CREATE VIEW people_with_author_name AS
SELECT
    p.people_id,
    p.people_name,
    p.author_id,
    a.author_name
FROM
    people p
JOIN
    author a ON p.author_id = a.author_id;



CREATE VIEW entity_with_tags AS
SELECT
  e.entity_id,
  e.content,
  e.create_at,
  e.start_time,
  e.author_id,
  e.related_people_id,
  e.activity,
  e.location,
  t.tag_id,
  t.tag_name,
  t.valence,
  t.parent_tag_id,
  t.category_id
FROM
  entity e
JOIN
  entity_tag_link l ON e.entity_id = l.entity_id
JOIN
  tag t ON l.tag_id = t.tag_id;