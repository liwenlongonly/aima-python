#!/bin/bash

searchs=(DFTS DFGS BFTS BFGS UCTS UCGS GBFTS GBFGS ASTS ASGS)

echo ${searchs[3]}

echo "map test"
for search in ${searchs[*]}
do
    echo "The search use: $search"
	  python map.py travel-input.txt $search
done
echo "map end"

echo "npuzzle test"
for search in ${searchs[*]}
do
    echo "The search use: $search"
	  python npuzzle.py npuzzle-input.txt $search
done

echo "npuzzle end"