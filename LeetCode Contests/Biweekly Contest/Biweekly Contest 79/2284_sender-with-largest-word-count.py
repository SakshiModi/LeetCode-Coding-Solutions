class Solution:
    def largestWordCount(self, messages, senders):
        sender_count={}
        n=len(senders)
        result=""
        for i in range(n):
            if senders[i] in sender_count:
                sender_count[senders[i]]+=len(messages[i].split(' '))
            else:
                sender_count[senders[i]]=len(messages[i].split(' '))
        largest_count=max(sender_count.values())
        for i in sender_count:
            if sender_count[i]==largest_count and i>result:
                result=i
        return result