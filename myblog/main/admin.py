from django.contrib import admin
from.models import Category,Post

# Register your models here.


#for configuration of category admin

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)







admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)

