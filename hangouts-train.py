import re

import hangups
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from hangouts_chat import run_example


async def get_conversation(client, args):
    request = hangups.hangouts_pb2.GetConversationRequest(
        request_header=client.get_request_header(),
        conversation_spec=hangups.hangouts_pb2.ConversationSpec(
            conversation_id=hangups.hangouts_pb2.ConversationId(
                id='Ugw5G0wDnE4uN945rJh4AaABAQ'
            ),
        ),
        include_event=True,
        max_events_per_conversation=10000,
    )
    res = await client.get_conversation(request)
    messages = re.findall(pattern='text:(.+)\n', string=str(res))

    print([message[2:-1] for message in messages])

    chatbot = ChatBot('Dr Buntu')
    trainer = ListTrainer(chatbot)
    trainer.train(conversation=[message[2:-1] for message in messages])


if __name__ == '__main__':
    run_example(get_conversation)
