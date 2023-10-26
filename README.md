# YH_bike_shop
 🚲 🚲

With more and more people taking to cycling in cities and towns, the demand for bikes has skyrocketed. Jumping on the trend you decide to leave the hustle and bustle of the rush hour commute and open a bike store!

Our store is going to be a full service, one stop shop for custom bikes, servicing, and repairs. That means we need to build them from the ground up!

> Every **bike** is made up of different **components**, these **components** have a **maximum lifespan** but that doesn't mean that every **component** will be in a perfect state - some maybe be previously used or even completely broken! Whenever a **bike** is taken out for a ride the **components** will deteriorate, and different types of bikes may cause their **components** to deteriorate at different rate.

### 💡 It is up to you to design your classes how you see fit, this includes the attributes and how your methods work. But remember all methods **must** be thoroughly tested using TDD.💡

---

### Virtual Environment Reminder

Before working on this repo, remember you'll need to create a virtual environment. To do this run the command

```sh
python -m venv venv
```

which should create a `venv` directory at the root of your project. Run the _activate_ binaries using

```sh
source venv/bin/activate
```

Don't forget to deactivate your virtual environment afterwards with:

```sh
deactivate
```

---

💡 You may want to use print statements along side returns to see your classes in action. By default, Pytest shows your print statements on failing tests. This is not super useful to see your great work in action. A handy flag to show your statements in your passing test suite would look like this:

```sh
PYTHONPATH=$(pwd) pytest -vrP test/test_file_name.py
```

This will then show your print statement on all passing tests. 💡

### Task 1 - Create a Component Class

Create a `Component` class. Each component will only have a certain lifespan (measured by the number of uses) and different components could have different lifespans.

A `Component` should have:

-   A way to track it's lifespan - we will need to know what it's `current_state` and `max_lifespan` are.

The `Component` class should have a `check_condition()` method:

-   `check_condition()` - This method should return the `current_state` of the `Component` and print a message with more detail - up to you how you implement but the state of the `Component` could range from "Pristine" and "Good" all the way to "Fragile" and "Broken" depending on the number of uses it has left.

---

### Task 2 - Create some Components

Now we have a `Component` class we can think about what components there might be.

 

-   `Bell`
-   `Brakes`
-   `Chain`
-   `Tyres`

As they are all types of `Components` they should inherit the methods and any attributes of the `Component` class.

Each `child` class should have a custom method that shows how each part is used and decreases the `current_state` of the component. Each part can only be used if it is not broken.

---

### Task 3:

Now that we have our parts, we can start building our bikes!

Bikes come in all shapes and sizes, so we'll need a `parent class` of `Bike` to get started. The `Bike` class should take the necessary instances of `Component` classes in it's constructor. Every `Bike` instance needs at least four components and a way to use the methods on each component.

Our bikes will also need a few methods:

-   `ride()` If all the components are in good working order, a customer can ride the bike.

    -   If all components are not broken, this should affect the `Bike` `Components`. Think about how this would affect the `Component` current state and maximum lifespan.
    -   If all the components are fine or pristine, this should return a print statement about the quality of the ride.
    -   If any are fragile but none are broken, this should return a different print statement about the quality of the ride.

-   `ring_bell()` This should return a print statement dependant on the status of the `Components`
    -   If all parts are fine or pristine, should return 'Ring! Ring! Ring!'
    -   If any `Components` are broken should return 'The bell fell off!'
    -   If any are fragile, but none are broken, should return 'Ring! cling...'

Great! We now have the core building blocks of what makes a bike. Use your `parent class` of `Bike` to make some different kinds of `Bike` to sell. We currently stock the types below:

-   `Racing`
-   `BMX`
-   `Mountain`
-   `Street`

`Racing` bikes will increase the wear on their `Tyres` and `Chain` 5% more per use.

`BMX` bikes don't have `Brakes` so their `Tyres` wear 15% more per use.

`Mountain` bikes have a 15% stronger `Chain`.

`Street` bikes increase the wear on their `Brakes` by 5% as all city riders stop at red lights.

---

### Task 4:

As a full service `Bike` shop, our customers need somewhere to go when their bikes need a spruce up or a full on repair. We need to hire a `Service_Person` to check over bikes, figure out if anything is wrong, service parts to make them pristine again, or order new parts to replace broken ones.

Create a `Service_Person` class with a property that tracks the current `Bike` that is being worked on. A `Service_Person` can only work on one bike at a time.

The `Service_Person` will need a few methods:

-   `order_parts()` This should replace any `broken` part to a new `pristine` one.

-   `service_parts()` This should change any `fragile` parts to `fine`.
-   `oil()` This should change any `Brakes`, `Chain` or `Gears` from `fine` to `pristine`.
-   `clean()` This should change the `Frame` from `fine` to `pristine`.
-   `pump_wheels()` This should change the state of `Tyres` from `fine` to `pristine`
-   `service_bike()` This should invoke the `service_parts()`, `oil()`, `pump_wheels()` and `clean()` methods.
-   `check_safety()` This method should ring the `Bike` bell and check that the `Brakes` are either `fine` or `pristine`.
-   `check_up()`:
    -   If any parts are broken, this should trigger the `order_parts()` method.
    -   If any parts are `fragile`, this should trigger the `service_parts()` method.
    -   If parts are either `fine`, or `pristine`, this should trigger the `service_bike()` method.
    -   Once all maintenance work is completed should trigger the `check_safety()` method to make those final safety checks and ring that all important bell of the freshly serviced `Bike`.

---

## Exceptions

Now we've built all our components, bikes and service team, its time we look at Exceptions and how to handle and test them. Let's put it into practice.

Have a look at the classes you've created and think about what could go wrong and how you might handle that? Here's a couple of ideas to get you started:

-   What if you try to test ride a bike with broken parts?
-   What if you try to ring a bell when the bike doesn't have one?
-   What if you try to oil a bike that doesn't have the required components?

> These are not the only things that could go wrong - use your imagination and look at what would happen if you try certain methods on bikes that don't have what is needed.

You can also think about creating your own custom errors.

## Extension tasks

1. Create some new `Components` such as electronics or forks. How would different bikes use these parts, would all bikes use these parts?

2. Create some new `Bike` classes. Our store could expand stock to folding bikes, e-bikes or even exercise! How would our `Service_Person` class need to service these new bikes?

3. If you complete all of these tasks, see the extensions folder for another task.
