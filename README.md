# Memory Leak Test

I use this simple container to demonstrate how Docker handles OOM errors. Be warned that this container will eventually use all memory it has access too! The process is low priority, and even if you don't mean to eat up all your RAM the kernel will probably kill this process before anything important. But, you've been warned. Either run this with a memory limit or prepare to be sad.

https://hub.docker.com/r/patricktcb/memleak