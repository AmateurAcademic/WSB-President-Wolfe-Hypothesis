# WSB-President-Wolfe-Hypothesis
Results from the first WSB hypothesis hackathon. There is a much better repo that came out since we have had our hackathon, please use [Caesurus' Short Volume](https://github.com/Caesurus/short_volume). 

## Hypothesis
The WSB President Wolfe Hypothesis came from this [post](https://www.reddit.com/r/wallstreetbets/comments/li5vch/i_think_i_found_a_way_to_predict_dips_with_nasdaq/). The post roughly states that the shorting volumes from 3 different sources (NASDAQ BX, NASDAQ PSX, FINA daily short volumes) can "sync", and when they do, the price of the stock goes down. A lot of people found this interesting on Wall Street Bets. I happened to comment on this post, and several DMs later, we had a team to build a scraper and analysis scripts. These are the graphs produced by the OP. 
 ![SNDL chart](https://preview.redd.it/2dj8tyjpqzg61.png?width=569&format=png&auto=webp&s=99aba3f5759d0272c401877acdef93cfea37e73d)
 
 ![second chart](https://preview.redd.it/f5a16zi7tzg61.png?width=657&format=png&auto=webp&s=d631425582fb2593c9041ecc90805bdd2e231861)
 
 ![TLRY chart](https://preview.redd.it/h5yrk8dof0h61.png?width=524&format=png&auto=webp&s=f7c89947359119453a375ee37a56578d524a18ed)
 
 ![TSLA chart](https://preview.redd.it/a01t7j8q41h61.png?width=458&format=png&auto=webp&s=a9ae45aa3c1bccc557f410a210ff331bd4039297)
 
 The hypothesis is easy to disprove by finding arbitary counter-examples. While tracking and especially normalizing shorting volumes can be a helpful indicator, there is no significant correlation between the 3 shorting volumes and the outcome on the price of the stock in terms of "syncing" behavior. 
 
 The sources of the data, as listed by the OP is the [NASDAQ Volume Files ftp://ftp.nasdaqtrader.com/files/shortsaledata/daily/](ftp://ftp.nasdaqtrader.com/files/shortsaledata/daily/) and [FINA Volume files](http://regsho.finra.org/regsho-Index.html).
