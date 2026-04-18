# Individual Reflections

## Birky Andrie Pacuribot — Sequential Sorting

Working on the sequential merge sort allowed me to clearly understand how divide-and-conquer algorithms operate in a step-by-step manner. The implementation was straightforward since it followed a predictable flow without the need to manage multiple processes. During testing, I observed that the algorithm performed consistently across all dataset sizes, but execution time increased significantly as the dataset became larger. One challenge I encountered was ensuring that the merge function correctly combined subarrays without losing order. Overall, this task showed me that while sequential algorithms are easier to implement and debug, they are limited in performance because they rely on a single processing unit.

## Carlos Jorge Gamale — Parallel Sorting

Implementing the parallel merge sort was more complex compared to the sequential version because it required dividing the dataset and managing multiple processes. I had to ensure that each process handled its portion correctly and that the final merge produced a globally sorted result. One of the main challenges was dealing with process overhead and understanding when parallelization actually improves performance. During testing, I noticed that parallel sorting did not always outperform sequential sorting, especially for smaller datasets. However, for larger datasets, the improvement became more noticeable. This experience helped me understand the trade-off between performance gains and the added complexity of parallel execution.

## Paul Vincent Noval — Sequential Searching

The sequential linear search was the simplest algorithm to implement in this project. It follows a direct approach by checking each element one at a time until the target is found. While it was easy to code and verify, I observed that its performance is not efficient for large datasets because it may require scanning the entire list. There were no major implementation issues, but testing highlighted its limitations in terms of scalability. This task reinforced the idea that simple algorithms are reliable but may not be suitable for large-scale data processing.

## Vonmar Viscayno — Parallel Searching

The parallel linear search introduced the concept of dividing the dataset and searching different parts simultaneously. Implementing this required careful handling of processes and communication between them, especially when returning the correct global index of the target. One challenge was ensuring that all processes terminated properly and that results were collected without conflicts. During testing, I observed that parallel search can reduce search time for large datasets, but the improvement is not always significant due to overhead. This task helped me understand how concurrency can improve performance, but also how it introduces additional complexity in synchronization and coordination.

## Ken Charles Besa — Dataset, Testing, and Integration

Handling dataset generation and testing gave me a broader view of how all components of the project work together. I was responsible for running experiments across different dataset sizes and analyzing the results. One key observation was that parallel algorithms are not always faster, particularly for small datasets where overhead dominates execution time. Managing the integration of different modules also required ensuring compatibility and correctness across all implementations. This role helped me understand the importance of testing, benchmarking, and organizing results to draw meaningful conclusions about algorithm performance.
