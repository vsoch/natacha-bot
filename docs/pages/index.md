---
layout: default
title: {{ site.name }}
permalink: /
excluded_in_search: true
---

<div style="float:right; margin-bottom:50px; color:#666">
</div>

<ol class="twitter-feed">
  {% assign n = site.wisdom | size %}
  {% assign posts = site.wisdom | sample: n %}
  {% for wisdom in posts %}<li class="tweet">
    <img class="profile-photo" src="{{ site.url }}{{ site.baseurl }}/natacha-bot.png" width="50px" />
    <p class="text-content">
    {{ wisdom.content | strip_html }}
    </p>
  </li>{% endfor %}
</ol>
