#!/bin/bash

# format - $name|$suffix|$models
readonly VARIANTS=(
  'all||en da de el es fr it lt nb nl pl pt ro'
  'da||da'
  'da|.md|da_core_news_md'
  'da|.lg|da_core_news_lg'
  'de||de'
  'de|.md|de_core_news_md'
  'de|.lg|de_core_news_lg'
  'el||el'
  'el|.md|el_core_news_md'
  'el|.lg|el_core_news_lg'
  'en||en'
  'en|.md|en_core_web_md'
  'en|.lg|en_core_web_lg'
  'es||es'
  'es|.md|es_core_news_md'
  'es|.lg|es_core_news_lg'
  'fr||fr'
  'fr|.md|fr_core_news_md'
  'fr|.lg|fr_core_news_lg'
  'it||it'
  'it|.md|it_core_news_md'
  'it|.lg|it_core_news_lg'
  'lt||lt'
  'lt|.md|lt_core_news_md'
  'lt|.lg|lt_core_news_lg'
  'nb||nb'
  'nb|.md|nb_core_news_md'
  'nb|.lg|nb_core_news_lg'
  'nl||nl'
  'nl|.md|nl_core_news_md'
  'nl|.lg|nl_core_news_lg'
  'pl||pl'
  'pl|.md|pl_core_news_md'
  'pl|.lg|pl_core_news_lg'
  'pt||pt'
  'pt|.md|pt_core_news_md'
  'pt|.lg|pt_core_news_lg'
  'ro||ro'
  'ro|.md|ro_core_news_md'
  'ro|.lg|ro_core_news_lg'
)

for variant in "${VARIANTS[@]}"; do
  IFS=$'|' read -r name suffix models <<< "$variant"
  mkdir -p "build/$name"
  sed -r "s!\{\{MODELS\}\}!$models!g; s!!ab!g;" docker/Dockerfile.template > "build/$name/Dockerfile$suffix"
done
