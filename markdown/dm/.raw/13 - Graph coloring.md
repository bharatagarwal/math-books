<!-- page 1 -->

![img-0.jpeg](13 - Graph coloring_images/img-0.jpeg)
Figure 40: Two-coloring the regions formed by a set of circles

# 13 Graph coloring

# 13.1 Coloring regions: an easy case

We draw some circles on the plane (say,  $n$  in number). These divide the plane into a number of regions. Figure 40 shows such a set of circles, and also an "alternating" coloring of the regions with two colors; it gives a nice pattern. Now our question is: can we always color these regions this way? We'll show that the answer is yes; to state this more exactly:

Theorem 13.1 The regions formed by  $n$  circles in the plane can be colored with read and blue so that any two regions that share a common boundary arc should be colored differently.

(If two regions have only one or two boundary points in common, then they may get the same color.)

Let us first see why a direct approach does not work. We could start with coloring the outer region, say blue; then we have to color its neighbors red. Could it happen that two neighbors are at the same time neighbors of each other? Perhaps drawing some pictures and then arguing carefully about them, you can design a proof that this cannot happen. But then we have to color the neighbors of the neighbors blue again, and we would have to prove that no two of these are neighbors of each other. This could get quite complicated! And then we would have to repeat this for the neighbors of the neighbors of the neighbors...

We should find a better way to prove this and, fortunately, there is a better way! We prove the assertion by induction on  $n$ , the number of circles. If  $n = 1$ , then we only get two regions, and we can color one of them red, the other one blue. So let  $n &gt; 1$ . Select any of the circles, say  $C$ , and forget about it for the time being. The regions formed by the remaining  $n - 1$  circles can be colored with red and blue so that regions that share a common boundary arc get different colors (this is just the induction hypothesis).

Now we take back the remaining circle, and change the coloring as follows: outside  $C$ , we leave the coloring as it was; inside  $C$ , we interchange red and blue (Figure 41).

It is easy to see that the coloring we obtained satisfies what we wanted. In fact, look at any small piece of arc of any of the circles. If this arc is outside  $C$ , then the two regions on its two sides were different and their colors did not change. If the arc is inside  $C$ , then again, the two regions on its both sides were differently colored, and even though their colors were switched, they are still different. Finally, the arc could be on  $C$  itself. Then

---

<!-- page 2 -->

![img-1.jpeg](13 - Graph coloring_images/img-1.jpeg)
Figure 41: Adding a new circle and recoloring

![img-2.jpeg](13 - Graph coloring_images/img-2.jpeg)

![img-3.jpeg](13 - Graph coloring_images/img-3.jpeg)
Figure 42: The proof of Euler's Theorem

the two regions on both sides of the arc were one and the same before putting  $C$  back, and so they had the same color. Now, one of them is inside  $C$  and this switched its color; the other is outside, and this did not. So after the recoloring, their colors will be different.

Thus we proved that the regions formed by  $n$  circles can be colored with two colors, provided the regions formed by  $n - 1$  circles can be colored with 2 colors. By the Principle of Induction, this proves the theorem.

13.1 Assume that the color of the outer region is blue. Then we can describe what the color of a particular region  $R$  is, without having to color the whole picture, as follows:

- if  $R$  lies inside an even number of circles, it will be colored blue;
- if  $R$  lies inside an odd number of circles, it will be colored red.

Prove this assertion.

13.2 (a) Prove that the regions, into which  $n$  straight lines divide the plane, are colorable with 2 colors.

(b) How could you describe what the color of a given region is?

---

<!-- page 3 -->

![img-4.jpeg](13 - Graph coloring_images/img-4.jpeg)
Figure 43: 4-coloring the countries

![img-5.jpeg](13 - Graph coloring_images/img-5.jpeg)
Figure 44: Proof of the 5-color theorem

![img-6.jpeg](13 - Graph coloring_images/img-6.jpeg)

---

<!-- page 4 -->

![img-7.jpeg](13 - Graph coloring_images/img-7.jpeg)
Figure 45: 4-coloring the countries and 3-coloring the edges

![img-8.jpeg](13 - Graph coloring_images/img-8.jpeg)
Figure 46: A graph and its dual