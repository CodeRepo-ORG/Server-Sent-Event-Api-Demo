# Server-Sent-Event-Api-Demo

This repository demonstrates the use of **Server-Sent Events (SSE)** using Python with the **FastAPI** framework and HTML for real-time data streaming. It provides an example of streaming updates from long-running tasks to a client through an HTTP connection.

---

## Table of Contents
- [What is SSE?](#what-is-sse)
- [How Does SSE Work?](#how-does-sse-work)
- [Features](#features)
- [API Overview](#api-overview)
- [Example Tasks](#example-tasks)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Applications](#applications)
- [License](#license)

---

## What is SSE?
**Server-Sent Events (SSE)** is a standard for enabling servers to push real-time updates to clients over HTTP. Unlike WebSockets, SSE is unidirectional, meaning the server can send updates to the client, but the client cannot send messages back.

SSE is often used for real-time notifications, progress updates, and monitoring logs.

---

## How Does SSE Work?
1. The client sends a `GET` request to the server for a resource that supports SSE.
2. The server keeps the connection open and streams data as events in plain text format.
3. Each event consists of optional fields such as `id`, `event`, and `data` to provide structured information.
4. The connection remains open until the server closes it or the client disconnects.

Example Event Format:
```
event: progress
data: Task is 50% complete

```

---

## Features
1. **FastAPI Backend** - A Python framework used to create and manage the server-side logic for event streaming.
2. **Streaming with SSE** - Implements Server-Sent Events to push data updates from the server to the client in real time.
3. **Task Simulation** - Demonstrates the execution of tasks with periodic updates during their processing.
4. **Event Handling** - Uses SSE-specific events like `start`, `progress`, `end`, and `close` for structured communication.

---

## API Overview
### Endpoint: `/stream`
- **Method:** `GET`
- **Response Type:** `text/event-stream`
- **Description:** Streams updates for two simulated tasks (`function1` and `function2`) with intermediate progress updates.

### Event Types:
1. **start** - Indicates the start of a task.
2. **progress** - Sends updates about ongoing progress.
3. **end** - Signals the completion of a task.
4. **close** - Marks the end of the event stream.

---

## Example Tasks
- **Task 1:** `function1()`
  - Simulates work with intermediate updates at 5-second intervals.
- **Task 2:** `function2()`
  - Similar to Task 1 but runs after Task 1 completes.

---

## Code Explanation
### Backend:
The server sends a sequence of events through a generator function `generate_json()` that yields event messages with IDs and data. Events include intermediate updates and signals for start, progress, end, and completion.

### Client-Side:
A client (HTML/JavaScript) can connect to the endpoint `/stream` to receive updates in real time without polling, as SSE maintains a persistent connection.

---

## Usage
1. Install dependencies:
```bash
pip install fastapi uvicorn
```
2. Run the server:
```bash
uvicorn main:app --reload
```
3. Access the API at:
```
http://localhost:8000/stream
```
4. Use an HTML client or a browser plugin to view the real-time updates.

---

## Applications
- Real-time notifications and progress updates.
- Monitoring background tasks.
- Streaming logs or analytics data.

---

## License
This project is open-source and available under the MIT License.

