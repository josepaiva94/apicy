#!/bin/bash

# format - $name|$suffix|$models
readonly VARIANTS=(
  'all||en_core_web_sm da_core_news_sm de_core_news_sm el_core_news_sm es_core_news_sm fr_core_news_sm it_core_news_sm lt_core_news_sm nb_core_news_sm nl_core_news_sm pl_core_news_sm pt_core_news_sm ro_core_news_sm'
  'da||da_core_news_sm'
  'da|.md|da_core_news_md'
  'da|.lg|da_core_news_lg'
  'de||de_core_news_sm'
  'de|.md|de_core_news_md'
  'de|.lg|de_core_news_lg'
  'el||el_core_news_sm'
  'el|.md|el_core_news_md'
  'el|.lg|el_core_news_lg'
  'en||en_core_web_sm'
  'en|.md|en_core_web_md'
  'en|.lg|en_core_web_lg'
  'es||es_core_news_sm'
  'es|.md|es_core_news_md'
  'es|.lg|es_core_news_lg'
  'fr||fr_core_news_sm'
  'fr|.md|fr_core_news_md'
  'fr|.lg|fr_core_news_lg'
  'it||it_core_news_sm'
  'it|.md|it_core_news_md'
  'it|.lg|it_core_news_lg'
  'lt||lt_core_news_sm'
  'lt|.md|lt_core_news_md'
  'lt|.lg|lt_core_news_lg'
  'nb||nb_core_news_sm'
  'nb|.md|nb_core_news_md'
  'nb|.lg|nb_core_news_lg'
  'nl||nl_core_news_sm'
  'nl|.md|nl_core_news_md'
  'nl|.lg|nl_core_news_lg'
  'pl||pl_core_news_sm'
  'pl|.md|pl_core_news_md'
  'pl|.lg|pl_core_news_lg'
  'pt||pt_core_news_sm'
  'pt|.md|pt_core_news_md'
  'pt|.lg|pt_core_news_lg'
  'ro||ro_core_news_sm'
  'ro|.md|ro_core_news_md'
  'ro|.lg|ro_core_news_lg'
)

for variant in "${VARIANTS[@]}"; do
  IFS=$'|' read -r name suffix models <<< "$variant"
  mkdir -p "build/$name"
  sed -r "s!\{\{MODELS\}\}!$models!g; s!!ab!g;" docker/Dockerfile.template > "build/$name/Dockerfile$suffix"
done
