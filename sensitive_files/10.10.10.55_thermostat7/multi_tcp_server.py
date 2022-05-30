import select, socket, sys, queue
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('0.0.0.0', int(sys.argv[1])))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}

try:
    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(131072)
                if len(data) > 0:
                    print("=== === === === === === ===")
                    print(data.decode("utf-8").replace('\\n', '\n'))
                if data:
                    # message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]

#        for s in writable:
#            try:
#                next_msg = message_queues[s].get_nowait()
#                pass
#            except queue.Empty:
#                outputs.remove(s)
#            else:
#                s.send(next_msg)

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]
except KeyboardInterrupt:
    for s in outputs:
        s.close()
    for s in inputs:
        s.close()
