#!/usr/bin/env bash

export BASE_URL='http://qa-recruitment-newsletter.s3-website-eu-west-1.amazonaws.com/'

behave -k -t runThis
