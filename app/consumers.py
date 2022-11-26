from channels.generic.websocket import AsyncConsumer

class Chatconsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.channel_layer.group_add(
            'publicchat',
            self.channel_name
        )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        if event:
            data = {
                'type':'chat.message',
                'message':event['text']
            }
            await self.channel_layer.group_send(
                'publicchat',
                data
            )
    
    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    async def websocket_disconnect(self, code):
        self.channel_layer.group_discard('publicchat',
            self.channel_name)