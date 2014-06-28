---
layout: page
title:  News
body_class: news
published: true
---

<h1> News</h1>
<!-- This loops through the paginated posts -->


{% for post in paginator.posts %}
  <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>

  <h6>{{ post.date | date: "%B %d, %Y" }}</h6>

  <div class="snippet">
    {{ post.content }}
  </div>
  <hr>
{% endfor %}

<!-- Pagination links -->
<div class="pagination">
  {% if paginator.previous_page %}
    {% if paginator.previous_page == 1 %}
      <a href="/news/index.html">Previous</a>
    {% else %}
      <a href="/news/page{{ paginator.previous_page }}/index.html" class="previous">Previous</a>
    {% endif %}
  {% else %}
    <span class="previous">Previous</span>
  {% endif %}
  <span class="page_number ">Page: {{ paginator.page }} of {{ paginator.total_pages }}</span>
  {% if paginator.next_page %}
    <a href="/news/page{{ paginator.next_page }}/index.html" class="next">Next</a>
  {% else %}
    <span class="next ">Next</span>
  {% endif %}
</div>
