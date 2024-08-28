-- create index for mulitple columns

create INDEX idx_name_first_score on names(name(0), score);
