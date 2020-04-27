#### 定义

>  Define a one-to-many dependency between objects so that when one object changes state,all its dependents are notified and updated automatically.

在对象间定义一种一对多的依赖关系，当这个对象状态发生改变时，所有依赖它的对象都会被通知并自动更新。

监听模式是一种一对多的关系，可以有任意个（一个或多个）观察者对象同时监听某一个对象。监听的对象叫观察者（后面提到监听者，其实就指观察者，两者是相同的），被监听的对象叫被观察者（Observable，也叫主题，即Subject）。被观察者对象在状态或内容（数据）发生变化时，会通知所有观察者对象，使它们能够做出相应的变化（如自动更新自己的信息）。

监听模式的核心思想就是在被观察者与观察者之间建立一种自动触发的关系。



