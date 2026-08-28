import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        # Global counter to act as a unique, increasing timestamp
        self.time = 0
        # Maps userId -> list of [timestamp, tweetId] (Appends preserve chronological order)
        self.user_tweets = defaultdict(list)  
        # Maps userId -> set of followeeIds
        self.following = defaultdict(set)     

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Save tweet with current timestamp, then advance time
        self.user_tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        max_heap = []
        
        # A user always implicitly follows themselves to see their own tweets
        self.following[userId].add(userId)
        
        # STEP 1: Put the single newest tweet of each followed user into the heap
        for followeeId in self.following[userId]:
            if followeeId in self.user_tweets:
                tweets = self.user_tweets[followeeId]
                last_index = len(tweets) - 1
                timestamp, tweetId = tweets[last_index]
                
                # Python heapq is a min-heap by default. 
                # We store negative timestamp (-timestamp) to turn it into a max-heap.
                # Format: (-timestamp, tweetId, followeeId, index of previous tweet)
                heapq.heappush(max_heap, (-timestamp, tweetId, followeeId, last_index - 1))
                
        # STEP 2: Extract up to 10 most recent tweets overall
        while max_heap and len(res) < 10:
            neg_time, tweetId, followeeId, prev_index = heapq.heappop(max_heap)
            res.append(tweetId)
            
            # If this followee has an older tweet remaining, push it onto the heap
            if prev_index >= 0:
                prev_time, prev_tweetId = self.user_tweets[followeeId][prev_index]
                heapq.heappush(max_heap, (-prev_time, prev_tweetId, followeeId, prev_index - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Prevent a user from unfollowing themselves
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)
