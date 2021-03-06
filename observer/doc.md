#### 定义

>  Define a one-to-many dependency between objects so that when one object changes state,all its dependents are notified and updated automatically.

在对象间定义一种一对多的依赖关系，当这个对象状态发生改变时，所有依赖它的对象都会被通知并自动更新。

监听模式是一种一对多的关系，可以有任意个（一个或多个）观察者对象同时监听某一个对象。监听的对象叫观察者（后面提到监听者，其实就指观察者，两者是相同的），被监听的对象叫被观察者（Observable，也叫主题，即Subject）。被观察者对象在状态或内容（数据）发生变化时，会通知所有观察者对象，使它们能够做出相应的变化（如自动更新自己的信息）。

监听模式的核心思想就是在被观察者与观察者之间建立一种自动触发的关系。



#### 设计要点

1. 要明确谁是观察者谁是被观察者，只要明白谁是应该关注的对象，问题也就明白了。一般观察者与被观察者之间是多对一的关系，一个被观察对象可以有多个监听对象（观察者）。如一个编辑框，有鼠标点击的监听者，也有键盘的监听者，还有内容改变的监听者。
2. Observable 在发送广播通知的时候，无须指定具体的 Observer,Observer 可以自己决定是否订阅Subject的通知。
3. 被观察者至少需要有三个方法：添加监听者、移除监听者、通知Observer的方法。观察者至少要有一个方法：更新方法，即更新当前的内容，做出相应的处理。
4. 添加监听者和移除监听者在不同的模型称谓中可能会有不同命名，如在观察者模型中一般是addObserver/removeObserver；在源/监听器（Source/Listener）模型中一般是attach/detach，应用在桌面编程的窗口中还可能是attachWindow/detachWindow或Register/UnRegister。不要被名称弄迷糊了，不管它们是什么名称，其实功能都是一样的，就是添加或删除观察者。



#### 推还是拉

监听模式根据其侧重的功能还可以分为推模型和拉模型。

##### 推模型

被观察者对象向观察者推送主题的详细信息，不管观察者是否需要，推送的信息通常是主题对象的全部或部分数据。一般在这种模型的实现中，会把被观察者对象中的全部或部分信息通过update参数传递给观察者（update（Object obj），通过obj参数传递）。

##### 拉模型

被观察者在通知观察者的时候，只传递少量信息。如果观察者需要更具体的信息，由观察者主动到被观察者对象中获取，相当于观察者从被观察者对象中拉数据。一般在这种模型的实现中，会把被观察者对象自身通过 update 方法传递给观察者(update(Observableobservable)，通过observable 参数传递），这样在观察者需要获取数据的时候，就可以通过这个引用来获取了。



推模型和拉模型其实更多的是语义和逻辑上的区别。我们前面的代码框架，从接口[update(self,observer,object)]上你应该可以知道是同时支持推模型和拉模型的。作为推模型时，observer可以传空，推送的信息全部通过object传递；作为拉模型时，observer和object都传递数据，或只传递observer，需要更具体的信息时通过observer引用去取数据。

















