from channels.routing import route
from channels import include
from chat_app.consumers import chat_connect, chat_disconnect, chat_receive, chathistory_connect, chathistory_disconnect, chathistory_receive

chat_routes = [
    route("websocket.connect", chat_connect),
    route("websocket.receive", chat_receive),
    route("websocket.disconnect", chat_disconnect)
]

chathistory_routes = [
    route("websocket.connect", chathistory_connect),
    route("websocket.receive", chathistory_receive),
    route("websocket.disconnect", chathistory_disconnect)
]

channel_routing = [
    include(chat_routes, path=r"^/chat/$"),
    include(chathistory_routes, path=r"^/chathistory/$"),
]