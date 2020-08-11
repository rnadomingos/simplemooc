from django.db import models


#MODO SIMPLES DE USAR QUERY_SET ** SEPARANDO O *_ICONTENS POR VIRGULA, O DJANGO CONSIDERA AND NA QUERY
    # class CourseManager (models.Manager):
    # def search(self, query):
    #     return self.get_queryset().filter(
    #         name_icontains=query, description_icontains=query
    #         ) 

class CourseManager (models.Manager):
        
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):

    name = models.CharField(("Nome"), max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Alterado em', auto_now=True)


    objects = CourseManager()

    def __str__(self):
        return self.name
    