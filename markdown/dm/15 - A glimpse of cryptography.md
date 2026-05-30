## 15 A glimpse of cryptography

## 15.1 Classical cryptography

Ever since writing was invented, people have been interested not only in using it to communicate with their partners, but also in trying to conceal the content of their message from their adversaries. This leads to cryptography (or cryptology), the science of secret communication.

The basic situation is that one party, say King Arthur, wants to send a message to King Bela. There is, however, a danger that the evil Caesar Caligula intercepts the message and learns things that he is not supposed to know about. The message, understandable even for Caligula, is called the plain text. To protect its content, King Arthur encrypts his message. When King Bela receives it, he must decrypt it in order to be able to read it. For the Kings to be able to encrypt and decrypt the message, they must know something that that the Caesar does not know: this information is the key.

Many cryptosystems have been used in history; most of them, in fact, turn out to be insecure, especially if the adversary can use powerful computing tools to break it.

Perhaps the simplest method is substitution code: we replace each letter of the alphabet by another letter. The key is the table that contains for each letter the letter to be substituted for it. While a message encrypted this way looks totally scrambled, substitution codes are in fact easy to break. Solving exercise 16.3 will make it clear how the length and positions of the words can be used to figure out the original meaning of letters, if the breaking into words is preserved (i.e., ”Space” is not replaced by another character). But even if the splitting into words is hidden, an analysis of the frequency of various letter gives enough information to break the substitution code.

We can watch that leak in action. The program below applies a random substitution cipher to a paragraph of English and then — using *no key material whatsoever* — recovers letters purely by matching symbol frequencies against the known frequencies of English:

```python
<!-- include: code/dm/15 - A glimpse of cryptography/01_python.py -->
```

It confirms the cipher is a perfect relabelling (decrypting with the true key is lossless), yet the plaintext and ciphertext share an *identical* frequency profile — and that profile alone recovers $231/562 \approx 41\%$ of the letters, far above the $1/26 \approx 4\%$ you would expect from guessing. The first line already emerges as a near-readable `tre olhenle if oelset liccgnhlathin…` (“the science of secret communication…”). On a longer message the recovery is essentially total — which is exactly why substitution ciphers are considered broken.
