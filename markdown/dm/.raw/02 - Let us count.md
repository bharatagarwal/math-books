<!-- page 1 -->

2 Let us count!

### 2.1 A party

Alice invites six guests to her birthday party: Bob, Carl, Diane, Eve, Frank and George. When they arrive, they shake hands with each other (strange European custom). This group is strange anyway, because one of them asks: “How many handshakes does this mean?”

“I shook 6 hands altogether” says Bob, “and I guess, so did everybody else.”

“Since there are seven of us, this should mean $7\cdot 6=42$ handshakes” ventures Carl.

“This seems too many” says Diane. “The same logic gives 2 handshakes if two persons meet, which is clearly wrong.”

“This is exactly the point: every handshake was counted twice. We have to divide 42 by 2, to get the right number: 21.” settles Eve the issue.

When they go to the table, Alice suggests:

“Let’s change the seating every half an hour, until we get every seating.”

“But you stay at the head of the table” says George, “since you have your birthday.”

How long is this party going to last? How many different seatings are there (with Alice’s place fixed)?

Let us fill the seats one by one, starting with the chair on Alice’s right. We can put here any of the 6 guests. Now look at the second chair. If Bob sits on the first chair, we can put here any of the remaining 5 guests; if Carl sits there, we again have 5 choices, etc. So the number of ways to fill the first two chairs is $5+5+5+5+5+5=6\cdot 5=30$. Similarly, no matter how we fill the first two chairs, we have 4 choices for the third chair, which gives $6\cdot 5\cdot 4$ ways to fill the first three chairs. Going on similarly, we find that the number of ways to seat the guests is $6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1=720$.

If they change seats every half an hour, it takes 360 hours, that is, 15 days to go through all seating orders. Quite a party, at least as the duration goes!

> 2.1 How many ways can these people be seated at the table, if Alice too can sit anywhere?

After the cake, the crowd wants to dance (boys with girls, remember, this is a conservative European party). How many possible pairs can be formed?

OK, this is easy: there are 3 girls, and each can choose one of 4 guys, this makes $3\cdot 4=12$ possible pairs.

After about ten days, they really need some new ideas to keep the party going. Frank has one:

“Let’s pool our resources and win a lot on the lottery! All we have to do is to buy enough tickets so that no matter what they draw, we should have a ticket with the right numbers. How many tickets do we need for this?”

(In the lottery they are talking about, 5 numbers are selected from 90.)

“This is like the seating” says George, “Suppose we fill out the tickets so that Alice marks a number, then she passes the ticket to Bob, who marks a number and passes it to Carl, …Alice has 90 choices, no matter what she chooses, Bob has 89 choices, so there are

---

<!-- page 2 -->

$90\cdot 89$ choices for the first two numbers, and going on similarly, we get $90\cdot 89\cdot 88\cdot 87\cdot 86$ possible choices for the five numbers.”

“Actually, I think this is more like the handshake question” says Alice. “If we fill out the tickets the way you suggested, we get the same ticket more then once. For example, there will be a ticket where I mark 7 and Bob marks 23, and another one where I mark 23 and Bob marks 7.”

Carl jumped up:

“Well, let’s imagine a ticket, say, with numbers $7,23,31,34$ and $55$. How many ways do we get it? Alice could have marked any of them; no matter which one it was that she marked, Bob could have marked any of the remaining four. Now this is really like the seating problem. We get every ticket $5\cdot 4\cdot 3\cdot 2\cdot 1$ times.”

“So” concludes Diane, “if we fill out the tickets the way George proposed, then among the $90\cdot 89\cdot 88\cdot 87\cdot 86$ tickets we get, every 5-tuple occurs not only once, but $5\cdot 4\cdot 3\cdot 2\cdot 1$ times. So the number of different tickets is only

$\frac{90\cdot 89\cdot 88\cdot 87\cdot 86}{5\cdot 4\cdot 3\cdot 2\cdot 1}.$

We only need to buy this number of tickets.”

Somebody with a good pocket calculator computed this value in a glance; it was 43,949,268. So they had to decide (remember, this happens in a poor European country) that they don’t have enough money to buy so many tickets. (Besides, they would win much less. And to fill out so many tickets would spoil the party…)

So they decide to play cards instead. Alice, Bob, Carl and Diane play bridge. Looking at his cards, Carl says: “I think I had the same hand last time.”

“This is very unlikely” says Diane.

How unlikely is it? In other words, how many different hands can you have in bridge? (The deck has 52 cards, each player gets 13.) I hope you have noticed it: this is essentially the same question as the lottery. Imagine that Carl picks up his cards one by one. The first card can be any one of the 52 cards; whatever he picked up first, there are 51 possibilities for the second card, so there are $52\cdot 51$ possibilities for the first two cards. Arguing similarly, we see that there are $52\cdot 51\cdot 50\cdot\ldots\cdot 40$ possibilities for the 13 cards.

But now every hand was counted many times. In fact, if Eve comes to quibbiz and looks into Carl’s cards after he arranged them, and tries to guess (I don’t now why) the order in which he picked them up, she could think: “He could have picked up any of the 13 cards first; he could have picked up any of the remaining 12 cards second; any of the remaining 11 cards third;… Aha, this is again like the seating: there are $13\cdot 12\cdot\ldots\cdot 2\cdot 1$ orders in which he could have picked up his cards.”

But this means that the number of different hands in bridge is

$\frac{52\cdot 51\cdot 50\cdot\ldots\cdot 40}{13\cdot 12\cdot\ldots\cdot 2\cdot 1}=635,013,559,600.$

So the chance that Carl had the same hand twice in a row is one in 635,013,559,600, very small indeed.

Finally, the six guests decide to play chess. Alice, who just wants to watch them, sets up 3 boards.

---

<!-- page 3 -->

How many ways can you guys be matched with each other?” she wonders. “This is clearly the same problem as seating you on six chairs; it does not matter whether the chairs are around the dinner table of at the three boards. So the answer is 720 as before.”

“I think you should not count it as a different matching if two people at the same board switch places” says Bob, “and it should not matter which pair sits at which table.”

“Yes, I think we have to agree on what the question really means” adds Carl. “If we include in it who plays white on each board, then if a pair switches places we do get a different matching. But Bob is right that it does not matter which pair uses which board.”

“What do you mean it does not matter? You sit at the first table, which is closest to the peanuts, and I sit at the last, which is farthest” says Diane.

“Let’s just stick to Bob’s version of the question” suggests Eve. “It is not hard, actually. It is like with handshakes: Alice’s figure of 720 counts every matching several times. We could rearrange the tables in 6 different ways, without changing the matching.”

“And each pair may or may not switch sides” adds Frank. “This means $2\cdot 2\cdot 2=8$ ways to rearrange people without changing the matching. So in fact there are $6\cdot 8=48$ ways to sit which all mean the same matching. The 720 seatings come in groups of 48, and so the number of matchings is $720/48=15$.”

“I think there is another way to get this” says Alice after a little time. “Bob is youngest, so let him choose a partner first. He can choose his partner in 5 ways. Whoever is youngest among the rest, can choose his or her partner in 3 ways, and this settles the matching. So the number of matchings is $5\cdot 3=15$.”

“Well, it is nice to see that we arrived at the same figure by two really different arguments. At the least, it is reassuring” says Bob, and on this happy note we leave the party.

> 2.2 What is the number of “matchings” in Carl’s sense (when it matters who sits on which side of the board, but the boards are all alike), and in Diane’s sense (when it is the other way around)?

### 2.2 Sets and the like

We want to formalize assertions like “the problem of counting the number of hands in bridge is essentially the same as the problem of counting tickets in the lottery”. The usual tool in mathematics to do so is the notion of a *set*. Any collection of things, called *elements*, is a set. The deck of cards is a set, whose elements are the cards. The participants of the party form a set, whose elements are Alice, Bob, Carl, Diane, Eve, Frank and George (let us denote this set by $P$). Every lottery ticket contains a set of 5 numbers.

For mathematics, various sets of numbers are important: the set of real numbers, denoted by $\mathbb{R}$; the set of rational numbers, denoted by $\mathbb{Q}$; the set of integers, denote by $\mathbb{Z}$; the set of non-negative integers, denoted by $\mathbb{Z}_{+}$; the set of positive integers, denoted by $\mathbb{N}$. The *empty set*, the set with no elements is another important (although not very interesting) set; it is denoted by $\emptyset$.

If $A$ is a set and $b$ is an element of $A$, we write $b\in A$. The number of elements of a set $A$ (also called the *cardinality* of $A$) is denoted by $|A|$. Thus $|P|=7$; $|\emptyset|=0$; and $|\mathbb{Z}|=\infty$ (infinity).

---

<!-- page 4 -->

We may specify a set by listing its elements between braces; so

$P=\{\text{Alice, Bob, Carl, Diane, Eve, Frank, George}\}$

is the set of participants of Alice’s birthday party, or

$\{12,23,27,33,67\}$

is the set of numbers on my uncle’s lottery ticket. Sometimes we replace the list by a verbal description, like

$\{\text{Alice and her guests}\}.$

Often we specify a set by a property that singles out the elements from a large universe like real numbers. We then write this property inside the braces, but after a colon. Thus

$\{x\in\mathbb{Z}:\ x\geq 0\}$

is the set of non-negative integers (which we have called $\mathbb{Z}_{+}$ before), and

$\{x\in P:\ x\text{ is a girl}\}=\{\text{Alice, Diane, Eve}\}$

(we denote this set by $G$). Let me also tell you that

$D=\{x\in P:\ x\text{ is over 21}\}=\{\text{Alice, Carl, Frank}\}$

(we denote this set by $D$).

A set $A$ is called a subset of a set $B$, if every element of $A$ is also an element of $B$. In other words, $A$ consists of certain elements of $B$. We allow that $A$ consists of all elements of $B$ (in which case $A=B$), or none of them (in which case $A=\emptyset$). So the empty set is a subset of every set. The relation that $A$ is a subset of $B$ is denoted by

$A\subseteq B.$

For example, among the various sets of people considered above, $G\subseteq P$ and $D\subseteq P$. Among the sets of numbers, we have a long chain:

$\emptyset\subseteq\mathbb{N}\subseteq\mathbb{Z}_{+}\subseteq\mathbb{Z}\subseteq\mathbb{Q}\subseteq\mathbb{R}$

The intersection of two sets is the set consisting of those elements that elements of both sets. The intersection of two sets $A$ and $B$ is denoted by $A\cap B$. For example, we have $G\cap D=\{Alice\}$. Two sets whose intersection is the empty set (in other words, have no element in common) are called disjoint.

> 2.3 Name sets whose elements are (a) buildings, (b) people, (c) students, (d) trees, (e) numbers, (f) points.
>
> 2.4 What are the elements of the following sets: (a) army, (b) mankind, (c) library, (d) the animal kingdom?

---

<!-- page 5 -->

2.5 Name sets having cardinality (a) 52, (b) 13, (c) 32, (d) 100, (e) 90, (f) 2,000,000.

2.6 What are the elements of the following (admittedly peculiar) set: $\{$Alice,$\{$1$\}$}\$?

2.7 We have not written up all subset relations between various sets of numbers; for example, $\mathbb{Z}\subseteq\mathbb{R}$ is also true. How many such relations can you find between the sets $\emptyset,\mathbb{N},\mathbb{Z}_{+},\mathbb{Z},\mathbb{Q},\mathbb{R}$?

2.8 Is an “element of a set” a special case of a “subset of a set”?

2.9 List all subsets of $\{0,1,3\}$. How many do you get?

2.10 Define at least three sets, of which $\{$Alice, Diane, Eve$\}$ is a subset.

2.11 List all subsets of $\{a,b,c,d,e\}$, containing $a$ but not containing $b$.

2.12 Define a set, of which both $\{1,3,4\}$ and $\{0,3,5\}$ are subsets. Find such a set with a smallest possible number of elements.

2.13 (a) Which set would you call the union of $\{a,b,c\}$, $\{a,b,d\}$ and $\{b,c,d,e\}$?

(b) Find the union of the first two sets, and then the union of this with the third. Also, find the union of the last two sets, and then the union of this with the first set. Try to formulate what you observed.

(c) Give a definition of the union of more than two sets.

2.14 Explain the connection beween the notion of the union of sets and exercise 2.2.

2.15 We form the union of a set with 5 elements and a set with 9 elements. Which of the following numbers can we get as the cardinality of the union: 4, 6, 9, 10, 14, 20?

2.16 We form the union of two sets. We know that one of them has $n$ elements and the other has $m$ elements. What can we infer for the cardinality of the union?

2.17 What is the intersection of

(a) the sets $\{0,1,3\}$ and $\{1,2,3\}$;

(b) the set of girls in this class and the set of boys in this class;

(c) the set of prime numbers and the set of even numbers?

2.18 We form the intersection of two sets. We know that one of them has $n$ elements and the other has $m$ elements. What can we infer for the cardinality of the intersection?

2.19 Prove that $|A\cup B|+|A\cap B|=|A|+|B|$.

2.20 The symmetric difference of two sets $A$ and $B$ is the set of elements that belong to exactly one of $A$ and $B$.

(a) What is the symmetric difference of the set $\mathbb{Z}_{+}$ of non-negative integers and the set $E$ of even integers ($E=\{\ldots-4,-2,0,2,4,\ldots$ contains both negative and positive even integers).

(b) Form the symmetric difference of $A$ ad $B$, to get a set $C$. Form the symmetric difference of $A$ and $C$. What did you get? Give a proof of the answer.

---

<!-- page 6 -->

2.3 The number of subsets

Now that we have introduced the notion of subsets, we can formulate our first general combinatorial problem: what is the number of all subsets of a set with $n$ elements?

We start with trying out small numbers. It plays no role what the elements of the set are; we call them $a,b,c$ etc. The empty set has only one subset (namely, itself). A set with a single element, say $\{a\}$, has two subsets: the set $\{a\}$ itself and the empty set $\emptyset$. A set with two elements, say $\{a,b\}$ has four subsets: $\emptyset,\{a\},\{b\}$ and $\{a,b\}$. It takes a little more effort to list all the subsets of a set $\{a,b,c\}$ with 3 elements:

$\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{b,c\},\{a,c\},\{a,b,c\}.$ (1)

We can make a little table from these data:

No. of elements 0 1 2 3 No. of subsets 1 2 4 8

Looking at these values, we observe that the number of subsets is a power of 2: if the set has $n$ elements, the result is $2^{n}$, at least on these small examples.

It is not difficult to see that this is always the answer. Suppose you have to select a subset of a set $A$ with $n$ elements; let us call these elements $a_{1},a_{2},\ldots,a_{n}$. Then we may or may not want to include $a_{1}$, in other words, we can make two possible decisions at this point. No matter how we decided about $a_{1}$, we may or may not want to include $a_{2}$ in the subset; this means two possible decisions, and so the number of ways we can decide about $a_{1}$ and $a_{2}$ is $2\cdot 2=4$. Now no matter how we decide about $a_{1}$ and $a_{2}$, we have to decide about $a_{3}$, and we can again decide in two ways. Each of these ways can be combined with each of the 4 decisions we could have made about $a_{1}$ and $a_{2}$, which makes $4\cdot 2=8$ possibilities to decide about $a_{1},a_{2}$ and $a_{3}$.

We can go on similarly: no matter how we decide about the first $k$ elements, we have two possible decisions about the next, and so the number of possibilities doubles whenever we take a new element. For deciding about all the $n$ elements of the set, we have have $2^{n}$ possibilities.

Thus we have proved the following theorem.

###### Theorem 2.1

A set with $n$ elements has $2^{n}$ subsets.

We can illustrate the argument in the proof by the picture in Figure 1.

We read this figure as follows. We want to select a subset called $S$. We start from the circle on the top (called a node). The node contains a question: is $a_{1}$ an element of $S$? The two arrows going out of this node are labeled with the two possible answers to this question (Yes and No). We make a decision and follow the appropriate arrow (also called an edge) to the the node at the other end. This node contains the next question: is $a_{2}$ an element of $S$? Follow the arrow corresponding to your answer to the next node, which contains the third (and in this case last) question you have to answer to determine the subset: is $a_{3}$ an element of $S$? Giving an answer and following the appropriate arrow we get to a node, which contains a listing of the elements of $S$.

Thus to select a subset corresponds to walking down this diagram from the top to the bottom. There are just as many subsets of our set as there are nodes on the last level.

---

<!-- page 7 -->

![img-0.jpeg](02 - Let us count_images/img-0.jpeg)
Figure 1: A decision tree for selecting a subset of  $\{a, b, c\}$ .

Since the number of nodes doubles from level to level as we go down, the last level contains  $2^{3} = 8$  nodes (and if we had an  $n$ -element set, it would contain  $2^{n}$  nodes).

Remark. A picture like this is called a tree. (This is not a mathematical definition, which we'll see later.) If you want to know why is the tree growing upside down, ask the computer scientists who introduced it, not us.

We can give another proof of theorem 2.1. Again, the answer will be made clear by asking a question about subsets. But now we don't want to select a subset; what we want is to enumerate subsets, which means that we want to label them with numbers  $0, 1, 2, \ldots$  so that we can speak, say, about subset No. 23 of the set. In other words, we want to arrange the subsets of the set in a list and the speak about the 23rd subset on the list.

(We actually want to call the first subset of the list No. 0, the second subset on the list No. 1 etc. This is a little strange but this time it is the logicians who are to blame. In fact, you will find this quite natural and handy after a while.)

There are many ways to order the subsets of a set to form a list. A fairly natural thing to do is to start with  $\emptyset$ , then list all subsets with 1 elements, then list all subsets with 2 elements, etc. This is the way the list (1) is put together.

We could order the subsets as in a phone book. This method will be more transparent if we write the subsets without braces and commas. For the subsets of  $\{a, b, c\}$ , we get the list

$\emptyset ,a,ab,abc,ac,b,bc,c.$

These are indeed useful and natural ways of listing all subsets. They have one shortcoming though. Imagine the list of the subsets of five elements, and ask yourself to name the 23rd subset on the list, without actually writing down the whole list. This will be difficult! Is there a way to make this easier?

Let us start with another way of denoting subsets (another encoding in the mathematical jargon). We illustrate it on the subsets of  $\{a, b, c\}$ . We look at the elements one by one, and write down a 1 if the element occurs in the subset and a 0 if it does not. Thus for

---

<!-- page 8 -->

the subset  $\{a, c\}$ , we write down 101, since  $a$  is in the subset,  $b$  is not, and  $c$  is in it again. This way every subset in "coded" by a string of length 3, consisting of 0's and 1's. If we specify any such string, we can easily read off the subset it corresponds to. For example, the string 010 corresponds to the subset  $\{b\}$ , since the first 0 tells us that  $a$  is not in the subset, the 1 that follows tells us that  $b$  is in there, and the last 0 tells us that  $c$  is not there.

Now such strings consisting of 0's and 1's remind us of the binary representation of integers (in other words, representations in base 2). Let us recall the binary form of nonnegative integers up to 10:

|  0 = 02  |
| --- |
|  1 = 12  |
|  2 = 102  |
|  3 = 2+1=112  |
|  4 = 1002  |
|  5 = 4+1=1012  |
|  6 = 4+2=1102  |
|  7 = 4+2+1=1112  |
|  8 = 10002  |
|  9 = 8+1=10012  |
|  10 = 8+2=10102  |

(We put the subscript 2 there to remind ourselves that we are working in base 2, not 10.)

Now the binary forms of integers  $0,1,\ldots,7$  look almost as the "codes" of subsets; the difference is that the binary form of an integer always starts with a 1, and the first 4 of these integers have binary forms shorter than 3, while all codes of subsets consist of exactly 3 digits. We can make this difference disappear if we append 0's to the binary forms at their beginning, to make them all have the same length. This way we get the following correspondence:

|  0 | ↔ | 02 | ↔ | 000 | ↔ | ∅  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | ↔ | 12 | ↔ | 001 | ↔ | {c}  |
|  2 | ↔ | 102 | ↔ | 010 | ↔ | {b}  |
|  3 | ↔ | 112 | ↔ | 011 | ↔ | {b,c}  |
|  4 | ↔ | 1002 | ↔ | 100 | ↔ | {a}  |
|  5 | ↔ | 1012 | ↔ | 101 | ↔ | {a,c}  |
|  6 | ↔ | 1102 | ↔ | 110 | ↔ | {a,b}  |
|  7 | ↔ | 1112 | ↔ | 111 | ↔ | {a,b,c}  |

So we see that the subsets of  $\{a,b,c\}$  correspond to the numbers  $0,1,\ldots ,7$

What happens if we consider, more generally, subsets of a set with  $n$  elements? We can argue just like above, to get that the subsets of an  $n$ -element set correspond to integers, starting with 0, and ending with the largest integer that has only  $n$  digits in its binary representation (digits in the binary representation are usually called bits). Now the smallest number with  $n + 1$  bits is  $2^n$ , so the subsets correspond to numbers  $0, 1, 2, \ldots, 2^n - 1$ . It is clear that the number of these numbers in  $2^n$ , hence the number of subsets is  $2^n$ .

---

<!-- page 9 -->

Comments. We have given two proofs of theorem 2.1. You may wonder why we needed two proofs. Certainly not because a single proof would not have given enough confidence in the truth of the statement! Unlike in a legal procedure, a mathematical proof either gives absolute certainty or else it is useless. No matter how many incomplete proofs we give, they don’t add up to a single complete proof.

For that matter, we could ask you to take our word for it, and not give any proof. Later in some cases this will be necessary, when we will state theorems whose proof is too long or too involved to be included in these notes.

So why did we bother to give any proof, let alone two proofs of the same statement? The answer is that every proof reveals much more than just the bare fact stated in the theorem, and this plus may be even more valuable. For example, the first proof given above introduced the idea of breaking down the selection of a subset into independent decisions, and the representation of this idea by a tree.

The second proof introduced the idea of enumerating these subsets (labeling them with integers $0,1,2,\ldots$). We also saw an important method of counting: we established a correspondence between the objects we wanted to count (the subsets) and some other kinds of objects that we can count easily (the numbers $0,1,\ldots,2^{n}-1$). In this correspondence

— for every subset, we had exactly one corresponding number, and

— for every number, we had exactly one corresponding subset.

A correspondence with these properties is called a one-to-one correspondence (or bijection). If we can make a one-to-one correspondence between the elements of two sets, then they have the same number of elements.

So we know that the number of subsets of a $100$-element set is $2^{100}$. This is a large number, but how large? It would be good to know, at least, how many digits it will have in the usual decimal form. Using computers, it would not be too hard to find the decimal form of this number, but let’s try to estimate at least the order of magnitude of it.

We know that $2^{3}=8<10$, and hence $2^{99}<10^{33}$. Therefore, $2^{100}<2\cdot 10^{33}$. Now $2\cdot 10^{33}$ is a $2$ followed by $33$ zeroes; it has $34$ digits, and therefore $2^{100}$ has at most $34$ digits.

We also know that $2^{10}=1024>1000=10^{3}$. Hence $2^{100}>10^{30}$, which means that $2^{100}$ has at least $30$ digits.

This gives us a reasonably good idea of the size of $2^{100}$. With a little more high school math, we can get the number of digits exactly. What does it mean that a number has exactly $k$ digits? It means that it is between $10^{k-1}$ and $10^{k}$ (the lower bound is allowed, the upper is not). We want to find the value of $k$ for which

$10^{k-1}\leq 2^{100}<10^{k}.$

Now we can write $2^{100}$ in the form $10^{x}$, only $x$ will not be an integer: the appropriate value of $x$ is $x=\lg 2^{100}=100\lg 2$. We have then

$k-1\leq x<k,$

---

<!-- page 10 -->

which means that $k-1$ is the largest integer not exceeding $x$. Mathematicians have a name for this: it is the integer part or floor of $x$, and it is denoted by $\lfloor x\rfloor$. We can also say that we obtain $k$ by rounding $x$ down to the next integer. There is also a name for the number obtained by rounding $x$ up to the next integer: it is called the ceiling of $x$, and denoted by $\lceil x\rceil$.

Using any scientific calculator (or table of logarithms), we see that $\lg 2\approx 0.30103$, thus $100\lg 2\approx 30.103$, and rounding this down we get that $k-1=30$. Thus $2^{100}$ has 31 digits.

> 2.21 Under the correspondence between numbers and subsets described above, which number correspond to subsets with 1 element?
>
> 2.22 What is the number of subsets of a set with $n$ elements, containing a given element?
>
> 2.23 What is the number of integers with (a) at most $n$ (decimal) digits; (b) exactly $n$ digits?
>
> 2.24 How many bits (binary digits) does $2^{100}$ have if written in base 2?
>
> 2.25 Find a formula for the number of digits of $2^{n}$.

### 2.4 Sequences

Motivated by the “encoding” of subsets as strings of 0’s and 1’s, we may want to determine the number of strings of length $n$ composed of some other set of symbols, for example, $a$, $b$ and $c$. The argument we gave for the case of 0’s and 1’s can be carried over to this case without any essential change. We can observe that for the first element of the string, we can choose any of $a$, $b$ and $c$, that is, we have 3 choices. No matter what we choose, there are 3 choices for the second of the string, so the number of ways to choose the first two elements is $3^{2}=9$. Going on in a similar manner, we get that the number of ways to choose the whole string is $3^{n}$.

In fact, the number 3 has no special role here; the same argument proves the following theorem:

###### Theorem 2.2

The number of strings of length $n$ composed of $k$ given elements is $k^{n}$.

The following problem leads to a generalization of this question. Suppose that a database has 4 fields: the first, containing an 8-character abbreviation of an employee’s name; the second, M or F for sex; the third, the birthday of the employee, in the format mm-dd-yy (disregarding the problem of not being able to distinguish employees born in 1880 from employees born in 1980); and the fourth, a jobcode which can be one of 13 possibilities. How many different records are possible?

The number will certainly be large. We already know from theorem 2.2 that the first field may contain $26^{8}>200,000,000,000$ names (most of these will be very difficult to pronounce, and are not likely to occur, but let’s count all of them as possibilities). The second field has 2 possible entries; the third, 36524 possible entries (the number of days in a century); the last, 13 possible entries.

Now how do we determine the number of ways these can be combined? The argument we described above can be repeated, just “3 choices” has to be replaced, in order, by

---

<!-- page 11 -->

“26^{8} choices”, “2 choices”, “36524 choices” and “13 choices”. We get that the answer is $26^{8}\cdot 2\cdot 36524\cdot 13=198307192370919424$.

We can formulate the following generalization of theorem 2.2

###### Theorem 2.3

Suppose that we want to form strings of length $n$ so that we can use any of a given set of $k_{1}$ symbols as the first element of the string, any of a given set of $k_{2}$ symbols as the second element of the string, etc., any of a given set of $k_{n}$ symbols as the last element of the string. Then the total number of strings we can form is $k_{1}\cdot k_{2}\cdot\ldots\cdot k_{n}$.

As another special case, consider the problem: how many non-negative integers have exactly $n$ digits (in decimal)? It is clear that the first digit can be any of 9 numbers $(1,2,\ldots,9)$, while the second, third, etc. digits can be any of the 10 digits. Thus we get a special case of the previous question with $k_{1}=9$ and $k_{2}=k_{3}=\ldots=k_{n}=10$. Thus the answer is $9\cdot 10^{n-1}$. (cf. with exercise 2.3).

- 2.26 Draw a tree illustrating the way we counted the number of strings of length 2 formed from the characters $a,b$ and $c$, and explain how it gives the answer. Do the same for the more general problem when $n=3$, $k_{1}=2$, $k_{2}=3$, $k_{3}=2$.
- 2.27 In a sport shop, there are T-shirts of 5 different colors, shorts of 4 different colors, and socks of 3 different colors. How many different uniforms can you compose from these items?
- 2.28 On a ticket for a succer sweepstake, you have to guess 1, 2, or X for each of 13 games. How many different ways can you fill out the ticket?
- 2.29 We roll a dice twice; how many different outcomes can we have (a 1 followed by a 4 is different from a 4 followed by a 1)?
- 2.30 We have 20 different presents that we want to distribute to 12 children. It is not required that every child gets something; it could even happen that we give all the presents to the same child. In how many ways can we distribute the presents?
- 2.31 We have 20 kinds of presents; this time, we have a large supply from each. We want to give presents to 12 children. Again, it is not required that every child gets something; but no child can get two copies of the same present. In how many ways can we give presents?

### 2.5 Permutations

During the party, we have already encountered the problem: how many ways can we seat $n$ people on $n$ chairs (well, we have encountered it for $n=6$ and $n=7$, but the question is natural enough for any $n$). If we imagine that the seats are numbered, then a finding a seating for these people is the same as assigning them to the numbers $1,2,\ldots,n$ (or $0,1,\ldots,n-1$ if we want to please the logicians). Yet another way of saying this is to order the people in a single line, or write down an (ordered) list of their names.

If we have an ordered list of $n$ objects, and we rearrange them so that they are in another order, this is called permuting them, and the new order is also called a permutation of the objects. We also call the rearrangement that does not change anything, a permutation (somewhat in the spirit of calling the empty set a set).

---

<!-- page 12 -->

![img-1.jpeg](02 - Let us count_images/img-1.jpeg)
Figure 2: A decision tree for selecting a subset of  $\{a, b, c\}$ .

For example, the set  $\{a,b,c\}$  has the following 6 permutations:

$$
a b c, a c b, b a c, b c a, c a b, c b a.
$$

So the question is to determine the number of ways  $n$  objects can be ordered, i.e., the number of permutations of  $n$  objects. The solution found by the people at the party works in general: we can put any of the  $n$  people on the first place; no matter whom we choose, we have  $n - 1$  choices for the second. So the number of ways to fill the first two positions is  $n(n - 1)$ . No matter how we have filled the first and second positions, there are  $n - 2$  choices for the third position, so the number of ways to fill the first three positions is  $n(n - 1)(n - 2)$ .

It is clear that this argument goes on like this until all positions are filled. The last but one position can be filled in two ways; the person put in the last position is determined, if the other positions are filled. Thus the number of ways to fill all positions is  $n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 2 \cdot 1$ . This product is so important that we have a notation for it:  $n!$  (read  $n$  factorial). In other words,  $n!$  is the number of ways to order  $n$  objects. With this notation, we can state our second theorem.

# Theorem 2.4 The number of permutations of  $n$  objects in  $n!$ .

Again, we can illustrate the argument above graphically (Figure 2). We start with the node on the top, which poses our first decision: whom to seat on the first chair? The 3 arrows going out correspond to the three possible answers to the question. Making a decision, we can follow one of the arrows down to the next node. This carries the next decision problem: whom to put on the second chair? The two arrows out of the node represent the two possible choices. (Note that these choices are different for different nodes on this level; what is important is that there are two arrows going out from each node.) If we make a decision and follow the corresponding arrow to the next node, we know who sits on the third chair. The node carries the whole "seating order".

It is clear that for a set with  $n$  elements,  $n$  arrows leave the top node, and hence there are  $n$  nodes on the next level.  $n - 1$  arrows leave each of these, hence there are  $n(n - 1)$  nodes on the third level.  $n - 2$  arrows leave each of these, etc. The bottom level has  $n!$  nodes. This shows that there are exactly  $n!$  permutations.

---

<!-- page 13 -->

2.32 $n$ boys and $n$ girls go out to dance. In how many ways can they all dance simultaneously? (We assume that only couples of different sex dance with each other.)

2.33 (a) Draw a tree for Alice’s solution of enumerating the number of ways 6 people can play chess, and explain Alice’s argument using the tree.

(b) Solve the problem for 8 people. Can you give a general formula for $2n$ people?

It is nice to know such a formula for the number of permutations, but often we just want to have a rough idea about how large it is. We might want to know, how many digits does $100!$ have? Or: which is larger, $n!$ or $2^{n}$? In other words, does a set with $n$ elements have more permutations or more subsets?

Let us experiment a little. For small values of $n$, subsets are winning: $2^{1}=2>1!=1$, $2^{2}=4>2!=2$, $2^{3}=8>3!=6$. But then the picture changes: $2^{4}=16<4!=24$, $3^{5}=32<5!=120$. It is easy to see that as $n$ increases, $n!$ grows much faster than $2^{n}$: if we go from $n$ to $n+1$, then $2^{n}$ grows by a factor of 2, while $n!$ grows by a factor of $n+1$.

This shows that $100!>2^{100}$; we already know that $2^{100}$ has 31 digits, and hence it follows that $100!$ has at least 31 digits.

What upper bound can we give on $n$!? It is trivial that $n!<n^{n}$, since $n!$ is the product of $n$ factors, each of which is at most $n$. (Since most of them are smaller than $n$, the product is in fact much smaller.) In particular, for $n=100$, we get that $100!<100^{100}=10^{200}$, so $100!$ has at most 200 digits.

In general we know that, for $n\geq 4$,

$2^{n}<n!<n^{n}.$

These bounds are rather weak; for $n=10$, the lower bound is $2^{10}=1024$ while the upper bound is $10^{10}$ (i.e., ten billion).

We could also notice that $n-9$ factors in $n!$ are greater than, or equal to 10, and hence $n!\geq 10^{n-9}$. This is a much better bound for large $n$, but it is still far from the truth. For $n=100$, we get that $100!\geq 10^{91}$, so it has at least 91 digits.

There is a formula that gives a very good approximation of $n!$. We state it without proof, since the proof (although not terribly difficult) needs calculus.

###### Theorem 2.5

[Stirling’s Formula]

$n!\sim\left(\frac{n}{e}\right)^{n}\sqrt{2\pi n}.$

Here $\pi=3.14\ldots$ is the area of the circle with unit radius, $e=2.718\ldots$ is the basis of the natural logarithm, and $\sim$ means approximate equality in the precise sense that on the one hand

$\frac{n!}{\left(\frac{n}{e}\right)^{n}\sqrt{2\pi n}}\rightarrow 1\qquad(n\rightarrow\infty).$

Both these funny irrational numbers $e$ and $\pi$ occur in the same formula!

So how many digits does $100!$ have? We know by Stirling’s Formula that

$100!\approx(100/e)^{100}\cdot\sqrt{200\pi}.$

---

<!-- page 14 -->

The number of digits of this number is its logarithm, in base 10, rounded up. Thus we get

$\lg(100!)\approx 100\lg(100/e)+1+\lg\sqrt{2\pi}=157.969\ldots$

So the number of digits in 100! is about 158 (actually, this is the right value).

2.34 (a) Which is larger, $n$ or $n(n-1)/2$?

(b) Which is larger, $n^{2}$ or $2^{n}$?

2.35 (a) Prove that $2^{n}>n^{3}$ if $n$ is large enough.

(b) Use (a) to prove that $2^{n}/n^{2}$ becomes arbitrarily large if $n$ is large enough.