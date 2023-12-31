# Queue
A Queue is an [Abstract Data Type](./CS50x_Abstract-Data-Type.md) collection of elements organized in sequence, which the elements are added from one end and removed from the other

```mermaid
flowchart LR
    subgraph enqueue
    6 
    end

    subgraph queue
     6 --> rear --- 5 --- 4 --- 3 --- 2 --- front
    end

    subgraph dequeue
        front --> 1
    end
```
## Operations
A Queue has 3 operations allowed to it:
- **Enqueue**: Adding an element to the last position of the queue (known as back, rear or tail).
- **Dequeue**: Remove an element from the first position of the queue (known as front).
- **Peek**: Return the value of the element in the first position of the queue without dequeuing it.

## Behavior
The behavior of a queue is described as First In, First Out, or the acronym FIFO. Elements can only be removed from the front of the queue, once an element is added all other elements in front of it must be removed first so it can be removed as well.


