#!/bin/bash
set -x

if [ -n "$CIRCLE_PULL_REQUEST" ]; then
    CHECKSTYLE_XML=$(git diff origin/master...HEAD | flake8 --diff --format=checkstyle)
    if [[ $CHECKSTYLE_XML = *error* ]]; then
        echo "$CHECKSTYLE_XML" | bundle exec saddler report \
            --require saddler/reporter/github \
            --reporter Saddler::Reporter::Github::PullRequestReviewComment
        echo "commented on $CIRCLE_PULL_REQUEST"
        exit 1
    fi
else
    echo "CIRCLE_PULL_REQUEST is empty"
fi
