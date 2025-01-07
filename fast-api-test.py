# from fastapi import FastAPI, Request
# from fastapi.responses import StreamingResponse
# from typing import Iterator
# import time

# app = FastAPI()

# # Helper function to simulate the tasks
# def function1():
#     time.sleep(5)
#     return "function1 completed successfully"

# def function2():
#     time.sleep(5)
#     return "function2 completed successfully"

# # Generate the SSE stream with event IDs
# def generate_json(request: Request) -> Iterator[str]:
#     # Event ID tracking
#     event_id = 0  # Start with event ID 0

#     # Simulate task 1
#     yield f"id: {event_id}\n"  # Start with ID for the first event
#     yield "event: start\n"
#     yield "data: function1 started\n\n"
#     event_id += 1

#     yield f"id: {event_id}\n"
#     yield "event: progress\n"
#     yield f"data: {function1()}\n\n"
#     event_id += 1

#     yield f"id: {event_id}\n"
#     yield "event: end\n"
#     yield "data: function1 ended\n\n"
#     event_id += 1

#     # Simulate task 2
#     yield f"id: {event_id}\n"
#     yield "event: start\n"
#     yield "data: function2 started\n\n"
#     event_id += 1

#     yield f"id: {event_id}\n"
#     yield "event: progress\n"
#     yield f"data: {function2()}\n\n"
#     event_id += 1

#     yield f"id: {event_id}\n"
#     yield "event: end\n"
#     yield "data: function2 ended\n"
#     yield "data: successfully function2 ended\n\n"
#     event_id += 1

#     # Send a signal to close connection
#     yield f"id: {event_id}\n"
#     yield "event: close\n"
#     yield "data: api completed\n\n"

# @app.get("/stream")
# async def stream_json(request: Request):
#     return StreamingResponse(generate_json(request), media_type="text/event-stream")
################################################################################################
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from typing import Iterator
import time

app = FastAPI()

# Modified function1 and function2 to yield intermediate updates
def function1():
    yield "function1 started"
    time.sleep(5)  # Simulate some work
    yield "function1 halfway done"
    time.sleep(5)  # Simulate more work
    yield "function1 completed successfully"

def function2():
    yield "function2 started"
    time.sleep(5)  # Simulate some work
    yield "function2 halfway done"
    time.sleep(5)  # Simulate more work
    yield "function2 completed successfully"

# Generate the SSE stream with event IDs
def generate_json(request: Request) -> Iterator[str]:
    event_id = 0  # Start with event ID 0

    # Simulate task 1
    yield f"id: {event_id}\n"  # Start with ID for the first event
    yield "event: start\n"
    yield "data: function1 started\n\n"
    event_id += 1

    # Yield intermediate results from function1
    for result in function1():
        yield f"id: {event_id}\n"
        yield "event: progress\n"
        yield f"data: {result}\n\n"
        event_id += 1

    yield f"id: {event_id}\n"
    yield "event: end\n"
    yield "data: function1 ended\n\n"
    event_id += 1

    # Simulate task 2
    yield f"id: {event_id}\n"
    yield "event: start\n"
    yield "data: function2 started\n\n"
    event_id += 1

    # Yield intermediate results from function2
    for result in function2():
        yield f"id: {event_id}\n"
        yield "event: progress\n"
        yield f"data: {result}\n\n"
        event_id += 1

    yield f"id: {event_id}\n"
    yield "event: end\n"
    yield "data: function2 ended\n\n"
    event_id += 1

    # Send a signal to close connection
    yield f"id: {event_id}\n"
    yield "event: close\n"
    yield "data: api completed\n\n"

@app.get("/stream")
async def stream_json(request: Request):
    return StreamingResponse(generate_json(request), media_type="text/event-stream")
