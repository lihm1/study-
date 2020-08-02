J <- list(name='JOE',salsry=55000,union=T)
class(J) <- "employee"
class(J) <- "a"
attributes(J)
print.a <- function(wrkr){
  cat(wrkr$name,"\n")
  cat("salary",wrkr$salary,"\n")
  cat("union member",wrkr$union,"\n")
}
