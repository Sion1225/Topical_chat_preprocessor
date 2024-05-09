# Topical_chat_preprocessor
This project was created to easily and conveniently preprocess the [Topical-Chat dataset](https://github.com/alexa/Topical-Chat) from the Amazon Alexa team.

The Topical-Chat dataset is already excellently organized in JSON files, but its structure is complex and the mixture of dictionary and list makes preprocessing inconvenient.

Therefore, it returns the data in various forms to facilitate use in ML and DS.

Currently, as a prototype, it only supports conversations data and returning data in list and dictonary type.

## Example code
```python
from topical_chat_preprocessor import TopicalChatPreprocessor

Tppre = TopicalChatPreprocessor('your Topical-Chat folder path')
listed_data = Tppre(['train','valid_freq','test_freq'])
```

## Expacted return 
### for argument 'list'
```
"return": [
  "files": [
    "article_url": [<url>, <url>, ...]
    "config": []
    "content_agent": [
      "agent": [<agent1>, <agent2>, ...]
    ]
    "content_message": [
      "message": [<text>, <text>, ...]
    ]
    "content_sentiment": [
      "sentiment": [<>, <>, ...]
    ]
    "content_knowledge_source": [
      "knowledge_source": [[<>], [<>, <>], ...]
    ]
    "content_turn_rating": [
      "turn_rating": [<>, <>, ...]
    ]
    "conversation_rating": {
      "agent_1": <>,
      "agent_2": <>
    }
  ]
]
```

### for argument 'dict'
```
"return": {
  "file name" <train>: {
    "article_url": [<url>, <url>, ...]
    "config": []
    "content_agent": [
      "agent": [<agent1>, <agent2>, ...]
    ]
    "content_message": [
      "message": [<text>, <text>, ...]
    ]
    "content_sentiment": [
      "sentiment": [<>, <>, ...]
    ]
    "content_knowledge_source": [
      "knowledge_source": [[<>], [<>, <>], ...]
    ]
    "content_turn_rating": [
      "turn_rating": [<>, <>, ...]
    ]
    "conversation_rating": {
      "agent_1": <>,
      "agent_2": <>
    }
  }
}
```
The difference is that the data for each file is now organized into a dictionary with the file name as the key `file_name: data`, and within each data, additional keys(`article_url`, `config`, `content_agent`, `content_message`, `content_sentiment`, `content_knowledge_source`, `content_turn_rating`, `conversation_rating`) are used based on specific names. Other than these changes, it remains similar to the list type.

## Reference
Gopalakrishnan, Karthik, et al. "Topical-Chat: Towards Knowledge-Grounded Open-Domain Conversations.", Proc. INTERSPEECH 2019
