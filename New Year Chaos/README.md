##New Year Chaos
###Problem Statement
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n = 8 and Person 5 bribes Person 4, the queue will look like this: [1, 2, 3, 5, 4, 6, 7, 8].

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

###Input Format:
The first line contains an integer t, the number of test cases.
Each of the next t pairs of lines are as follows:
- The first line contains an integer t, the number of people in the queue
- The second line has n space-separated integers describing the final state of the queue. 

###Sample Input:
<pre><code>2
5
2 1 5 3 4
5
2 5 1 3 4
</pre></code>

###Sample Output:
<pre><code>3
Too chaotic</code></pre>

###Solution steps
* Initial approach:
My first thought was to simply count the number of mismatched stickers, i.e., the number of stickers which did not match with the position they were at. There was a sticker-validity check where if the difference between the sticker and it's position was greater than 2 it would return **'Too chaotic'**.
This did not work because it did not incorporate scenarios where there was multi-level bribing. This refers to a person who has already accepted a bribe and then bribed someone else. Something like this: [1, 2, 5, 3, 7, 8, 6, 4]. This approach would not have worked for person 6 standing in the 7th position of the queue.
* Final solution:
At this point it was obvious that actually tracing the movements of each person in the queue could not be avoided. The program initializes a new queue called __tracer__ which is used to trace out each movement of each person in ascending order of their sticker numbers.
The program reverse engineers the movements of each person and increments the counter each time there is a movement. The positions are updated in __tracer__. This functionality is part of a _reduce_ function which collects the results in a dict object called __result__. __result__ holds the count of the movements made for the queue to reach it's current state, the validity of the state of the queue and the __tracer__ queue for the sake of maintaining the changes made to the __tracer__ queue.


###Problem statement link
https://www.hackerrank.com/challenges/new-year-chaos/problem?filter=Cisco&filter_on=company&h_l=interview&limit=100&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
