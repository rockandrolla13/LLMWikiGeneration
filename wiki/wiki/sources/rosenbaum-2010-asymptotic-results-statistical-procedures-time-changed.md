---
authors:
- Mathieu Rosenbaum
- Peter Tankov
content_hash: sha256:77891978b3684e4f1628bd4c84e625cf4178680902a8f162883cb2bdd02d7c56
created: 2026-09-27 01:47:00+00:00
page_id: sources/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed
page_type: source
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/stochastic-time-change
revision_id: 1
schema_version: 2
source_hash: sha256:cf15e7310e6811fafb4a7b9e47e0ac15bc80370f8185a4e5f7672bbca67a04e6
source_path: markdown_output/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed.md
source_type: paper
tags:
- levy-processes
- hitting-times
- stable-processes
- time-change
- jump-activity
- asymptotic-theory
- high-frequency-statistics
- clock-intrinsic
- asset-simulated
- harvest-relevant
title: Asymptotic results and statistical procedures for time-changed Lévy processes
  sampled at hitting times
updated: '2026-09-27T01:47:00Z'
uuid: 742fc8af-b4e7-5546-aae0-dfc0a936fe03
year: 2010
---

<!-- AUTHORED REGION START -->
# Asymptotic results and statistical procedures for time-changed Lévy processes sampled at hitting times

## Summary

The paper studies a one-dimensional Lévy process observed only at random instants defined as the first hitting times of a symmetric barrier of width epsilon around the last recorded value, rather than at fixed calendar times. This is motivated as a first, stylised step toward modelling tick-by-tick financial data that can include large jumps, with the barrier interpreted as something like a bid-ask interval.

Under a rescaling of the process in both space (by epsilon inverse) and time (by an exponent of epsilon depending on the process), the authors classify Lévy processes into five cases and show that in each case the rescaled process converges in law to a strictly alpha-stable process as epsilon goes to zero. This classification is shown to cover essentially all Lévy models used in finance, including diffusion-based models, the variance gamma model, the normal inverse Gaussian process, and the CGMY process.

The convergence is then extended to the moments of the hitting time itself and to functionals of the overshoot (the process value at the hitting time), with explicit convergence rates obtained under extra regularity conditions on the Lévy measure. These limit results are used to build a law of large numbers for time-averaged functionals of the observed hitting times and overshoots, from which the authors construct a consistent estimator of the underlying time change and, for the time-changed CGMY process, a consistent estimator of the Blumenthal-Getoor index that governs the intensity of small jumps. A multidimensional central limit theorem then gives the asymptotic distribution of vectors of such estimators in two of the five classification cases; in a third case, where the exit is dominated by a deterministic drift, only a convergence-rate bound rather than a central limit theorem is obtained.

The contribution is presented as extending prior work on random, endogenous sampling schemes -- previously studied only for continuous processes -- to a setting that explicitly allows for jumps, and as a first step toward statistical inference for financial data sampled at hitting-time-based, non-calendar intervals.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations occur at first hitting times of a symmetric barrier of width epsilon around the last observed value -- a threshold-crossing scheme in the spirit of directional-change sampling -- rather than at fixed calendar times, with epsilon shrunk to zero as the asymptotic parameter. The paper does not define a fixed forecast horizon; instead it characterises the limiting law, as epsilon goes to zero, of the rescaled process, of the hitting time itself, and of the overshoot past the barrier at the hitting time, and uses these limits to construct estimators of the time change and of jump-activity parameters.

## Data

- **Asset class:** Simulated data
- **Instruments:** not stated (a general one-dimensional Lévy process model; motivated by tick-by-tick financial data with a bid-ask-interval interpretation, but no data is analysed)
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated (purely theoretical paper; no dataset is used)

## Features and Measures

- **Rescaled Lévy process.** The original Lévy process rescaled in space by epsilon inverse and in time by an exponent of epsilon, whose limiting law as epsilon goes to zero defines the stable process used for the asymptotic theory.
- **First hitting time of a barrier.** The first time the rescaled process leaves the interval (-1,1); its moments and limiting distribution are used to construct the time-change estimator.
- **Overshoot at the hitting time.** The value of the rescaled process at the moment it exits the barrier interval, whose distribution is combined with the hitting time to estimate the Blumenthal-Getoor index of jump activity.

## Method

The paper first classifies Lévy processes into five cases, indexed by a stability parameter alpha and conditions on the diffusion coefficient, drift and Lévy measure, under which a rescaled version of the process converges in law to a strictly alpha-stable process. It then proves convergence of the moments of the first hitting time of a symmetric barrier, and of bounded continuous functionals of the overshoot, to the corresponding quantities for the limiting stable process, with explicit convergence rates under additional Hölder-type conditions on the Lévy density. These convergence results are turned into a law of large numbers for time-averaged functionals of the observed hitting times and overshoots, from which the time-change estimator and the Blumenthal-Getoor index estimator are built. A multidimensional central limit theorem then gives the asymptotic distribution of vectors of such estimators. The whole analysis proceeds through mathematical propositions, theorems and proofs, with no simulation study or empirical data.

## Results

- For a broad class of Lévy processes -- all models with a nonzero diffusion component, all finite-variation processes with nonzero drift, and most parametric jump models used in finance -- the appropriately rescaled process converges in law to a strictly alpha-stable process as the barrier width epsilon goes to zero.
- The first hitting time of the barrier and its overshoot converge, together with their moments, to those of the limiting stable process; explicit convergence rates are established under additional Hölder-type conditions on the Lévy density.
- A law of large numbers is proved for time-averages of bounded continuous functionals of the observed hitting times and overshoots, holding uniformly on compact time sets in probability.
- These limit results yield a consistent estimator of the time change (playing the role of the integrated volatility in this setting) recovered directly from the observed hitting times.
- For the time-changed CGMY process, the same approach yields a consistent estimator of the Blumenthal-Getoor index of jump activity, built from moments of the overshoot at the hitting times.
- A multidimensional central limit theorem establishes asymptotic normality of the renormalised estimation error under two of the five classification cases; under the case where the exit is dominated by a deterministic drift, only a convergence-rate bound rather than a central limit theorem can be obtained.

## Limitations

- The results are purely theoretical: no simulation study or empirical application to real tick-by-tick data is presented.
- The authors state that a detailed financial interpretation of the model, and modifying it so that observed values remain on a discrete tick grid, are left for further research.
- Under the classification case where the process exits deterministically (drift-dominated), no central limit theorem can be established for the resulting estimator, only a convergence-rate bound.
- Reader note: the barrier-hitting sampling scheme studied is one-dimensional and symmetric, so it is not shown here whether the results extend to asymmetric or multi-dimensional order-book-style triggers.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]

## Citation

Mathieu Rosenbaum, Peter Tankov (2010). Asymptotic results and statistical procedures for time-changed Lévy processes sampled at hitting times.

DOI: 10.48550/arxiv.1007.1414

Text ingested: `markdown_output/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed.md`, converted from `raw/ofi-event-clock/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed.pdf`.

Coverage of this summary: Read the full markdown file, including the introduction and motivation, the classification of Lévy processes and convergence-in-law results, the exit-time and overshoot convergence and rate results, the law-of-large-numbers and estimator constructions, the central limit theorem, and skimmed the proofs and reference list.

Known problems with the input: No year, journal or venue name, or author affiliations beyond the single shared institution line are printed anywhere in the extracted text; the year is taken from the job file's year_hint as instructed; The markdown replaces almost all inline mathematical notation and equations with 'picture intentionally omitted' placeholders, so the mathematical content is described only qualitatively rather than reproduced; Diacritics are OCR-garbled throughout (e.g. 'Lévy' appears as 'L´evy'); names and terms are reproduced here with the intended spelling.
<!-- AUTHORED REGION END -->