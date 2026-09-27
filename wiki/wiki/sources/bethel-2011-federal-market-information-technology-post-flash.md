---
authors:
- E. Wes Bethel
- David Leinweber
- Oliver Rubel
- Kesheng Wu
content_hash: sha256:8681bc3eff6e3345120ebcad8786e392c64f378f075304699f241ee337fe7795
created: 2026-09-27 01:47:00+00:00
page_id: sources/bethel-2011-federal-market-information-technology-post-flash
page_type: source
related:
- concepts/sampling-clocks
- concepts/informed-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/vpin
- entities/e-wes-bethel
- entities/david-leinweber
- entities/kesheng-wu
revision_id: 1
schema_version: 2
source_hash: sha256:2d420de6d664ddbfe2d63ac93fe9e38eb6402e9b6f0cfa43f65147bef3abfebd
source_path: markdown_output/bethel-2011-federal-market-information-technology-post-flash.md
source_type: paper
tags:
- vpin
- market-fragmentation
- flash-crash
- hpc
- hdf5
- early-warning-system
- circuit-breakers
- taq-data
- clock-compares
- asset-equity
- harvest-relevant
title: 'Federal Market Information Technology in the Post Flash Crash Era: Roles for
  Supercomputing'
updated: '2026-09-27T01:47:00Z'
uuid: 05c96079-5474-5d09-a7b1-d1c06a6b453d
year: 2011
---

<!-- AUTHORED REGION START -->
# Federal Market Information Technology in the Post Flash Crash Era: Roles for Supercomputing

## Summary

The paper describes a collaboration between traders, regulators, economists and supercomputing researchers at Lawrence Berkeley National Laboratory's Center for Innovative Financial Technology (CIFT) to replicate and extend investigations of the May 6, 2010 Flash Crash using high-performance computing (HPC). The motivating question is whether a graduated, 'yellow light' early-warning approach, rather than blunt on/off circuit breakers, could give regulators advance signals of dangerous market conditions.

The authors implement two published early-warning indicators - Volume-Synchronized Probability of Informed Trading (VPIN) and a volume-based Herfindahl-Hirschman Index (HHI) of market fragmentation - computed from Trades And Quotes (TAQ) transaction data reorganized into the HDF5 scientific data format and indexed with the FastBit/FastQuery bitmap-indexing software. They test whether HPC-style data organization and parallel (manager-worker) task distribution can make these computations fast enough for near-real-time regulatory monitoring, and they build an interactive query and visualization tool for analysts to inspect warning periods against historical data.

Both VPIN and HHI show sharp, elevated readings ahead of and during the May 6, 2010 Flash Crash for individual stocks (ACN, CNP, HPQ, AAPL) and ETFs (SPY, IWM). Storing data in HDF5 rather than CSV sharply cuts both storage size and computation time, and parallelizing the independent per-stock computations across many processing elements yields substantial further speedups, as does using bitmap-indexed queries to locate and extract warning periods from historical data.

What is new is not a new indicator but a demonstration that data-intensive-science techniques from HPC (HDF5 storage with SZIP compression, FastBit bitmap indexing, parallel manager-worker scheduling, and query-driven visualization) can make computing these already-known market-toxicity and fragmentation indicators, and searching historical warning periods, fast enough to be operationally useful for a federal market early-warning system.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

VPIN buckets trades into equal-volume bins (volume-time) rather than equal-time bins, then computes a buy/sell volume imbalance normalized through the cumulative normal distribution function so a single threshold (0.9) can apply across instruments. HHI is instead computed on fixed 5-minute calendar bins as the sum of squared exchange trade-volume shares, compared against a trailing one-hour reference window of preceding bins to flag a reading as abnormal. Neither indicator uses limit-order-book or order-flow message data, and both are computed per stock or fund as a same-day early-warning signal rather than a forecast of a specific future return.

## Data

- **Asset class:** Equities
- **Instruments:** Individual S&P 500 stocks (case studies: Accenture ACN, CenterPoint Energy CNP, Hewlett-Packard HPQ, Apple AAPL) and two ETFs (SPY, IWM); plus a broader run over all S&P 500 stocks and the 25 largest-volume ETFs
- **Venue:** U.S. equity markets, via consolidated Trades And Quotes (TAQ) data
- **Period:** First dataset: April-May 2010 (45 trading days), covering the May 6, 2010 Flash Crash; second dataset: 25 ETFs spanning 3 to 10 years (2001-2010) depending on the ETF
- **Granularity:** Trade-level (tick) data; VPIN computed on equal-volume buckets, HHI computed on 5-minute calendar bins

## Features and Measures

- **VPIN (Volume-Synchronized Probability of Informed Trading).** A measure of buy/sell trade-volume imbalance computed over equal-volume (rather than equal-time) buckets and normalized via the normal cumulative distribution function so a common threshold applies across stocks; used as an early-warning signal of order-flow toxicity.
- **Volume HHI (market fragmentation index).** The sum of squared shares of trading volume executed at each exchange within a fixed time bin (5 minutes here); a value near 1 means trading is concentrated at a single venue, while lower values indicate fragmentation across venues.

## Method

The authors reorganize TAQ trades and quotes data into HDF5 files (grouped by data type, date and stock symbol, with SZIP compression) and build FastBit bitmap indexes over these files via the FastQuery software, comparing storage size and query/computation time against plain CSV. VPIN and HHI are computed independently per stock or fund using a manager-worker parallel scheduling scheme across processing elements on the NERSC 'Hopper' HPC system, since the per-stock computations do not depend on each other.

Performance is judged by wall-clock computation time versus the number of processing elements used (for VPIN/HHI computation and for evaluating large batches of symbolic date/symbol queries), and by comparing file size and read/query speed between CSV, compressed CSV, HDF5, and SZIP-compressed HDF5. An interactive spreadsheet-style tool lets an analyst browse automatically generated warning events (with duration and peak-value color-coding) and pull up the underlying trade/quote time series for manual verification.

## Results

- VPIN and HHI both showed elevated readings ahead of and during the May 6, 2010 Flash Crash for the stocks and ETFs examined (ACN, CNP, HPQ, AAPL, SPY, IWM), with a single threshold of 0.9 on the normalized VPIN value (equivalent to 1.645 standard deviations for the HHI anomaly test) able to flag warnings across instruments.
- For Accenture (ACN), both HHI and VPIN spiked sharply at 13:35, about 70 minutes before the Flash Crash, coinciding with an unusually large 470,300-share trade at 13:36:07.
- Storing three days of S&P 500 trades and quotes in HDF5 instead of CSV shrank file sizes from 2,769 MB (trades) and 38,566 MB (quotes) in CSV to 1,326 MB and 28,844 MB in HDF5, and further to 472 MB and 5,377 MB with SZIP compression.
- Computing VPIN for Accenture took 142 seconds from CSV files versus 0.4 seconds from HDF5 files, a 355-fold speedup attributed to faster, more targeted data access.
- Parallelizing the independent per-stock VPIN/HHI computations gave up to 11x (HHI) and 13x (VPIN) speedups on S&P 500 data using 128 processing elements, and up to 5x on 25 ETFs using 8 processing elements.
- Evaluating 8000 date/symbol queries on a 74.5 GB April 2010 S&P 500 quotes dataset took about 3.5 hours in serial with CSV but under 5 seconds in parallel with indexed HDF5, a roughly 6,300x combined speedup; a 10-times-replicated 744.7 GB version of the same dataset still completed in under 5 seconds.
- The 45-trading-day (April-May 2010) S&P 500 dataset and a 25-ETF dataset spanning 3 to 10 years (2001-2010) covering about 2.7 billion trade records (108 GB CSV / 17 GB HDF5) were both used to test the indicators and the data pipeline.
- Screening S&P 500 stocks for HHI-based anomalies during April 2010 alone produced 298,956 potential warning events, illustrating the scale of data the interactive query tool needed to help analysts sift through.

## Limitations

- The authors state the two indicators use only trade (and, for the interactive tool, quote) data, not limit-order-book or order-flow message data, so the study is described by the authors as a modest example of what a full operational system would require.
- The case study is limited in scope to TAQ data and to computing already-published indicators (VPIN, HHI), rather than validating new indicators or building a complete real-time production system.
- The authors note unresolved data-quality problems, for example disagreement between TAQ, Nanex, and the SEC/CFTC report on how many AAPL trades occurred at $100,000 per share on May 6, 2010.
- Reader note: the paper reports indicator behavior around a single historical event (the May 6, 2010 Flash Crash) and does not report a systematic false-positive/false-negative evaluation of the warning signals.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/vpin|VPIN]]
- [[entities/e-wes-bethel|E. Wes Bethel]]
- [[entities/david-leinweber|David Leinweber]]
- [[entities/kesheng-wu|Kesheng Wu]]

## Citation

E. Wes Bethel, David Leinweber, Oliver Rubel, Kesheng Wu (2011). Federal Market Information Technology in the Post Flash Crash Era: Roles for Supercomputing.

DOI: 10.2139/ssrn.1939522

Text ingested: `markdown_output/bethel-2011-federal-market-information-technology-post-flash.md`, converted from `raw/ofi-event-clock/bethel-2011-federal-market-information-technology-post-flash.pdf`.

Coverage of this summary: Read the whole paper: abstract, introduction, background on LBNL/CIFT and levels of market data, the market-indicators (VPIN, HHI) description, the data-management/HDF5 section, the full case study section (file format, computing market indicators, and query-driven analysis subsections), discussion, future work, conclusion, acknowledgments, and reference list.

Known problems with the input: One sentence describing total record counts for the first (S&P 500, April-May 2010) dataset is cut off mid-number ('about 640') in the markdown conversion, so that figure is not used; The document is formatted as an LBNL technical report with a DOE disclaimer and does not print a journal or conference name on the document itself, even though the text references a related SC11 workshop; venue is left blank rather than inferred.
<!-- AUTHORED REGION END -->