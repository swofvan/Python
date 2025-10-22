# You are building a basic dashboard for a blog website.
# The blog has a list that stores the number of viewsfor different blog posts.

# Your task is to:
# Loop through the given list of blog post views.
# For each blog post:
# If views > 1000, print "Trending"
# If views between 500 and 1000, print "Average"
# If views < 500, print "Low Traffic"

# After the loop:
# Print the total number of views
# Print how many posts were "Trending"
# Use this list for blog views:
# blog_views = [150, 800, 2500, 600, 1200, 450, 3000]


blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

trend = 0     # for Trending post

for views in blog_views:
    if views > 1000:
        print("Trending")
        trend += 1                                   # for increacing Trending post
    elif views >= 500 and views <= 1000 :
        print("Average")
    else:
        print("Low Traffic")

total_views = sum(blog_views)
print("total views : ", total_views)

print("Trending Posts : ", trend)