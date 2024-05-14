test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = sorted(set(test_design_writers + test_scripters + reviewers))
script_only_testers = sorted(set(test_scripters) - set(test_design_writers) - set(reviewers))
at_work_today = sorted(set(all_testers) - set(out_of_office_today))
write_review_at_work = sorted(set(test_scripters) & set(reviewers) & set(at_work_today))

print("All testers in the team")
print(all_testers)
print("\nTesters who can only write scripts")
print(script_only_testers)
print("\nTesters who are at work today")
print(at_work_today)
print("\nTesters who could write and review scripts, and are at work today")
print(write_review_at_work)