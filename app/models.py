from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=True)
    describtion = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=100)
    job = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} // {self.author}"

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    is_solved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} -- {self.email}"

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=100,blank=True)
    message = models.TextField()

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} // {self.email}"
