context('add_one')

add_one <- function(x) {
  x + 1.1
}

test_that('adding one to one makes two', {
  expect_equal(add_one(1), 2)
})
