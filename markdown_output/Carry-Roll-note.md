## Carry & Roll 

## Nordea Research, 12 July 2013 

**Lars Peter Lilleøre** Chief Analyst Head of Rates & Volatility Strategy +45 3333 1470 lars.peter.lilleore@nordea.com 

## **Introduction** 

In this note we define how we look at carry and roll on standard interest rate swaps. The extension to bonds and other linear products is straightforward. Options will require a separate set of assumptions. 

Carry and roll are related but fundamentally different. We define _carry_ to be a certain number, and _roll_ to be an uncertain number, subject to specific assumptions being met. 

Carry for a certain horizon is equal to the certain payment(s) encountered over that period, i.e. payments known at the current time. 

Roll for a certain horizon is equal to the value appreciated simply by letting time elapse, i.e. it is the “return” stemming from a future curve being equal to today’s curve. It is _not_ an expectation. 

Carry & roll can be given in relative or absolute terms. These are related by dv01. For instance, if the par rate rolls 10bp then the absolute roll is (first order) approximated by 10*dv01. For comparison across maturities, the relative measure is to be preferred. 

Receiver positions typically have positive carry & roll, as is the case for long bond positions. The notions are often grouped together as “roll+carry”. 

As examples we consider two receiver swaps, EUR[1] 5Y spot and 6M5Y, i.e. a 5Y EUR swap, 6 month forward. We consider 6M roll and carry[2] . 

## **Notation** 

- ( ) 

   - Forward Swap rate at time t, for swap running from to . The 5Y spot rate is then (    ) . 

- ( ) 

   - Fixing for the period from to . (     ) is the 6m Euribor fixing in 6 months’ time, and F(0,6m) is the current 6m fixing. 

- ( ) 

Swap with fixed rate K running from to . If ( ) , this has zero PV. If K is omitted, the Swp in question is atmf. 

- 1 For convenience we assume everywhere in the following that the currency is EUR and that 

- swap conventions match that. 

## **Contents** 

Introduction ................................ 1 Notation ...................................... 1 Spot starting swaps, carry: ....... 2 Roll, forward or spot starting: ... 2 Graphical illustration of roll & carry ............................................ 3 Numeric examples: ................... 4 Appendix..................................... 5 

- 2 This is the most “natural” period to consider as it matches both the forward period and the 

- float-leg payment schedule. “Unnatural” periods are considered briefly at the end of the note. 

nordeamarkets.com/research 

Carry & Roll 

## **Spot starting swaps, carry:** 

Only spot starting swaps have a known fixing, F(0,6m). There’s no carry in a forward starting swap as there’s no certain payments (on the float leg). 

In a spot starting receiver swap (forward value of) carry is 


![](markdown_output/Carry-Roll-note_images/Carry-Roll-note.pdf-0002-04.png)


( ) ( ) 

in 6 month’s time. This is an absolute number and depends on no assumptions[3] . For an increasing term structure this number simply increases in the length of the swap. To that end, we use (1a) as our primary carry measure: 


![](markdown_output/Carry-Roll-note_images/Carry-Roll-note.pdf-0002-07.png)


This number is often approximated by: 


![](markdown_output/Carry-Roll-note_images/Carry-Roll-note.pdf-0002-09.png)


which lends itself to some nice graphics and is fine for periods equal to or less than the fixing period, but is erroneous for larger periods, see appendix. Note that both (1a) and (1b) give Carry in annualized yield terms. For absolute values (also known to some as upfront carry), simply multiply with dv01(Swp(6m,4½Y)). 

## **Roll, forward or spot starting:** 

Roll is defined as the number implied by freezing the current curve, and reducing the maturity of the swap tail or letting part of the forward period elapse. For 5Y spot: 


![](markdown_output/Carry-Roll-note_images/Carry-Roll-note.pdf-0002-13.png)


For 6M5Y: 


![](markdown_output/Carry-Roll-note_images/Carry-Roll-note.pdf-0002-15.png)


Both numbers imply a completely static curve and are contingent on that. Both numbers can be thought of as a buffer against market movements, but neither ensures the receiver swap holder anything. Finally, these numbers are in (swap) rate/yield terms and must be scaled with dv01 for absolute returns, i.e. with dv01(Swp(0,4½Y)).[4] 

> 3 Counterparty risks etc. are another class of risk relative to the purpose of this note. The ½ in the formula is the coverage (in practice the value is subject to day count convention etc), 4 This will be an approximation. Convexity is overlooked as is the not so small time increment. 

research.nordeamarkets.com 

2 

Carry & Roll 

## Nordea™ 

## **Graphical illustration of roll & carry** 

Both roll and carry can be given intuitively as distances between curves. For a spot starting swap, e.g. Swp(0d,5Y) carry and roll are given be the highlighted differences below (increasing forward periods on the x-axis). 

Roll and Carry on 5Y receiver spot swap 

For forward starting swaps, there’s no carry, and roll simply entails reducing the forward period. That is, Swp(6M,5Y) becomes Swp(0d,5Y). Similarly, e.g. Swp(1Y,5Y) becomes Swp(6M,5Y). 

Roll on 6M5Y receiver swap 

~~SUE~~ research.nordeamarkets.com 

3 

Carry & Roll 

## **Numeric examples:** 

It is instructional to establish where the numbers in the chart above come from. Per close 14/6/2013, we had the following values 

(    ) (     ) (      ) (      ) (    ) 

Given these values, 6M roll becomes (1.023% - 0.928%) = 9.5bps by (2a). Carry is by (1a) 

Similarly, (1b) gives (1.1015%-1.023%) = 7.9bps. 

Carry is sound here, and as long as one only uses (1b) on certain payments. When this is the case, roll and carry are additive; the former is contingent on the curve being unchanged, whereas the carry has no curve assumption. 

## 2s5s flattener 

Again for 14/6/2013 consider a 2s5s 6m fwd flattener: Receive 6M5Y and pay 6M2Y in ratio 1:2.48 (dv01-neutral) with 100m notional in 6M5Y. The risk is then 4.93 (dv01 on the 6M5Y swap) on both the receiver and payer legs of the trade. 

The relevant rates for roll calculation are 

(     ) (    ) (     ) (    ) 

For the dv01-neutral 2s5s, the roll thus is 

(1.195% - 1.023%) – (0.632%-0.498%) = 3.7bps. 

These are additive (without scaling) because they’re on the same initial risk (4.93). Put differently, if the curve turns out to be same on 14/12/2013, the profit of the flattener is (to a first order approximation) 3.7bps*4.93 = 18.24bps, or 182400 on the 100m:248m trade given above. 

research.nordeamarkets.com 

4 

Carry & Roll 

## **Appendix** 

Comments on non-standard Roll&Carry (read only if interest for full detail): 

The most natural roll period is equal or less than the payment frequency of the swap. However, variations such as 6M roll on a 1Y5Y swap poses no difficulties, just use (2b). 

However, situations may arise where one will look at 12M carry+roll on a spot swap, or say 6M roll on a 3M5Y swap. This leaves a problem. 

The problem lies with carry. Per definition carry only applies to the first certain payment. 1Y roll on a 5Y spot starting swap can be inferred by (2a). Carry for the first payment is given by (1a), but the payment referring to the fixing F[6M,1Y] is floating in no-man’s land. Under the carry approximation of (1b) the current implied future fixing is used. Under roll assumption the fixing will equal the current fixing F[0,6M]. Naturally, both cannot be true, and if the situation arises, we will take this fixing to be unchanged as the rest of the curve. 

Thus, the wheels comes off when longer carry periods are attempted, e.g. 1Y. Indeed, carry+roll here (using the approximate carry method) is (SR(0,5Y)SR(0,4Y))+(SR(1Y,4Y)-SR(0,5Y)) for a total of SR(1Y,4Y)-SR(0,4Y). 

The problem is that the current 4Y rate and the expected 4Y rate in 1 year’s time (forwards realized) are non-additive. The resulting 4Y rate cannot be both the current 4Y (roll assumption) and the 1Y4Y (carry assumption) rate.[5] 

The problem is equivalent for 6M roll on a 3M5Y. Again the fixing F[3M, 9M] in unknown and needs an assumption. 

Problem is solved by only looking at natural horizon periods. But, if 1Y roll is to be considered on a spot starting swap, use roll assumptions (i.e. curve unchanged, including the fixing). Never use the carry approximation (1b) for horizons in excess of the fixing period. 

Nordea Markets is the name of the Markets departments of Nordea Bank Norge ASA, Nordea Bank AB (publ), Nordea Bank Finland Plc and Nordea Bank Danmark A/S. The information provided herein is intended for background information only and for the sole use of the intended recipient. The views and other information provided herein are the current views of Nordea Markets as of the date of this document and are subject to change without notice. This notice is not an exhaustive description of the described product or the risks related to it, and it should not be relied on as such, nor is it a substitute for the judgement of the recipient. 

The information provided herein is not intended to constitute and does not constitute investment advice nor is the information intended as an offer or solicitation for the purchase or sale of any financial instrument. The information contained herein has no regard to the specific investment objectives, the financial situation or particular needs of any particular recipient. Relevant and specific professional advice should always be obtained before making any investment or credit decision. It is important to note that past performance is not indicative of future results. Nordea Markets is not and does not purport to be an adviser as to legal, taxation, accounting or regulatory matters in any jurisdiction. This document may not be reproduced, distributed or published for any purpose without the prior written consent from Nordea Markets. 

> 5 There is one special curve form that satisfies this. 

research.nordeamarkets.com 

5 

