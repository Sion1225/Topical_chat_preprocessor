# Topical_chat_preprocessor
This project was created to easily and conveniently preprocess the [Topical-Chat dataset](https://github.com/alexa/Topical-Chat) from the Amazon Alexa team.

The Topical-Chat dataset is already excellently organized in JSON files, but its structure is complex and the mixture of dictionary and list makes preprocessing inconvenient.

Therefore, it returns the data in various forms to facilitate use in ML and DS.

Currently, as a prototype, it only supports returning data in list type.

## Example code
```python
from topical_chat_preprocessor import TopicalChatPreprocessor

Tppre = TopicalChatPreprocessor('your Topical-Chat folder path')
listed_data = Tppre(['train','valid_freq','test_freq'])
```
