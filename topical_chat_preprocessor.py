import json
import os

class TopicalChatPreprocessor:
    """Class for preprocessing Topical Chat

    Args:
        topical_cat_dir (str): The path of the Topical_chat folder.

    Note:
        Still building.
    """
    def __init__ (self, topical_chat_dir:str = "Topical_chat/"):
        self.topical_chat_dir = topical_chat_dir

    def topical_chat_conversations_extractor(self, ):
        # Open the conversations
        conv_path = os.path.join(self.topical_chat_dir, 'conversations')

        self.topical_raw_data = []
        for _file_name in self.target_data: # Considering multi-processing
            file_name = _file_name + '.json'
            try:
                with open(os.path.join(conv_path, file_name)) as f:
                    self.topical_raw_data.append(json.load(f))
            except FileNotFoundError:
                raise ValueError(f"There isn't {file_name} in the path {conv_path}.")
            except json.JSONDecodeError:
                raise ValueError(f"File {file_name} is not a valid JSON file.")
        

        if self.output_type == 'list':
            output = []
            for data in self.topical_raw_data:
                article_url = []
                config = []
                content_agent = []
                content_message = []
                content_sentiment = []
                content_knowledge_source = []
                content_turn_rating = []
                conversation_rating = [] #: keep original dictonary

                for key in data.keys():
                    article_url.append(data[key]['article_url'])
                    config.append(data[key]['config'])

                    agent = []
                    message = []
                    sentiment= []
                    knowledge_source = []
                    turn_rating = []
                    for content in data[key]['content']:
                        agent.append(content['agent'])
                        message.append(content['message'])
                        sentiment.append(content['sentiment'])
                        knowledge_source.append(content['knowledge_source'])
                        turn_rating.append(content['turn_rating'])

                    content_agent.append(agent)
                    content_message.append(message)
                    content_sentiment.append(sentiment)
                    content_knowledge_source.append(knowledge_source)
                    content_turn_rating.append(turn_rating)
                    conversation_rating.append(data[key]['conversation_rating'])

                output.append([article_url, config, content_agent, content_message, content_sentiment, content_knowledge_source, content_turn_rating, conversation_rating])

            #logging.debug("Return.")
            return output
                
        
    def __call__(self, target_data:list = ['train', 'valid_freq', 'valid_rare'], output_type:str = 'list'):
        """
        Args:
            target_data (tuple, list): target data for process. e.g.) ('train', 'test_freq'). default is ('train', 'valid_freq', 'valid_rare')
            output_type (str): Output type of return. default is list.

        Returns:
            list['output_type']: extracted topical chat data.

        Note:
            Still making so there is only one option for 'output_type'.
        """
        self.output_type = output_type
        self.target_data = target_data

        if output_type == 'list':
            return self.topical_chat_conversations_extractor()
        else:
            raise ValueError("Unexpected Value")