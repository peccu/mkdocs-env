#!/bin/bash

function index(){
cat <<EOF >index.md
# Index $1, $2, $3

## toctree(.)

{{ toctree('.') }}

## toctree(., 1)

{{ toctree('.', 1) }}

## toctree(., 2)

{{ toctree('.', 2) }}

## listfiles(.)

- {{ listfiles('.') }}

## test(.)

- {{ test('.') }}
EOF
}

function page(){
cat <<EOF >page_0${1}_0${2}_0${3}_0${4}.md
# Page headings $1, $2, $3, $4

page contents

{{ toctree('.') }}

page contents
EOF

}

for i in 1 2 3 4
do
  echo Chapter 0$i
  mkdir -p chapter_0$i
  cd chapter_0$i
  index $i

  for j in 1 2 3 4
  do
    echo Section 0$j
    mkdir -p section_0$j
    cd section_0$j
    index $i $j

    for k in 1 2 3 4
    do
      echo SubSection 0$k
      mkdir -p subsection_0$k
      cd subsection_0$k
      index $i $j $k

      for l in 1 2 3 4
      do
        page $i $j $k $l
      done

      cd ..
      page $i $j $k
    done

    cd ..
    page $i $j
  done

  cd ..
  page $i
done