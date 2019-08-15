<div align="center">
<pre>
    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
         
</pre>
</div>

# CLI - Garfield comics downloader
[![Build Status](https://travis-ci.com/Bartosz-D3V/garfield-downloader.svg?token=tqZyPRhzSnop7iN2Y7Ug&branch=master)](https://travis-ci.com/Bartosz-D3V/garfield-downloader)

Simple CLI for quick & concurrent Garfield comics download.

## Heading Pre-requisites

Software installed and added to a class path (as a system variable):
 1. Python
 2. Pipenv installed globally
 
 ## Installing
 Before working with the CLI, install dependencies using pipenv:

    pipenv install

## Options

>   CLI for concurrent downloading comics from garfield.com    Options: 
> 
>   --start_date [%d/%m/%Y|%d-%m-%Y|%Y/%m/%d|%Y-%m-%d]  
>                                   Starting date of comics to download  
>                                   
>   --end_date [%d/%m/%Y|%d-%m-%Y|%Y/%m/%d|%Y-%m-%d]  
>                                   Ending date of comics to download  
>                                   
>   --path PATH                     Path to save the comics  
>   
>   --help                          Show this message and exit.


## Running tests
In order to run tests, please execute the following command:

    pipenv run pytest

## Lint
In order to run linting, please execute the following command:

    pipenv run pylint garfield_downloader tests
