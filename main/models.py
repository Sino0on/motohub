from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    subtitle = models.CharField(max_length=255, verbose_name='Второе название', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    secondary_description = models.TextField(verbose_name='Второе описание', blank=True, null=True)
    image1 = models.ImageField(upload_to='services/', verbose_name='Изображение 1')
    image2 = models.ImageField(upload_to='services/', verbose_name='Изображение 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='services/', verbose_name='Изображение 3', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    icon = models.CharField(max_length=255, verbose_name='Иконка')
    counter = (models.PositiveIntegerField(verbose_name='Счетчик'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(verbose_name='Мини описание')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение')
    svg = models.FileField(verbose_name='SVG', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    profession = models.CharField(max_length=255, verbose_name='Профессия')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='testimonials/', verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    work_scope = models.CharField(max_length=255, verbose_name='Объем работ')
    secondary_description = RichTextField(verbose_name='Второе описание', blank=True, null=True)
    client = models.CharField(max_length=255, verbose_name='Клиент')
    dimensions = models.CharField(max_length=255, verbose_name='Размеры', blank=True, null=True)
    location = models.CharField(max_length=255, verbose_name='Локация')
    type = models.CharField(max_length=255, verbose_name='Тип')
    image1 = models.ImageField(upload_to='projects/', verbose_name='Изображение 1')
    image2 = models.ImageField(upload_to='projects/', verbose_name='Изображение 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='projects/', verbose_name='Изображение 3', blank=True, null=True)
    image4 = models.ImageField(upload_to='projects/', verbose_name='Изображение 4', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(verbose_name='Мини описание')
    description = RichTextField(verbose_name='Описание')
    main_image = models.ImageField(upload_to='news/', verbose_name='Главное изображение')
    author = models.CharField(max_length=255, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    profession = models.CharField(max_length=255, verbose_name='Профессия')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='banners/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.title


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Если модель уже существует, удалите ее
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Если модель еще не существует, создайте ее
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class SiteSetting(SingletonModel):
    contacts = models.TextField(blank=True, verbose_name='Контакт')
    emails = models.TextField(blank=True, verbose_name='Почта')
    title = models.CharField(max_length=123, blank=True, null=True, verbose_name='Название компании')
    photo_video = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Название компании')
    description = RichTextField(blank=True, null=True, verbose_name='О нас')
    hours = models.CharField(max_length=123, verbose_name='Рабочие часы')
    director = models.CharField(max_length=123, verbose_name='Генеральный директор')
    video = models.URLField(verbose_name='Ссылка на ютуб')
    address = models.CharField(max_length=123, verbose_name="Адрес")
    address_map = models.TextField( verbose_name="Адрес на карте", default='''
    <a class="dg-widget-link" href="http://2gis.kg/bishkek/firm/70000001021088130/center/74.587426,42.845011/zoom/16?utm_medium=widget-source&utm_campaign=firmsonmap&utm_source=bigMap">Посмотреть на карте Бишкека</a><div class="dg-widget-link"><a href="http://2gis.kg/bishkek/firm/70000001021088130/photos/70000001021088130/center/74.587426,42.845011/zoom/17?utm_medium=widget-source&utm_campaign=firmsonmap&utm_source=photos">Фотографии компании</a></div><div class="dg-widget-link"><a href="http://2gis.kg/bishkek/center/74.587426,42.845011/zoom/16/routeTab/rsType/bus/to/74.587426,42.845011╎Кыргызский Государственный Технический Университет им. И. Раззакова, ректорат?utm_medium=widget-source&utm_campaign=firmsonmap&utm_source=route">Найти проезд до Кыргызский Государственный Технический Университет им. И. Раззакова, ректорат</a></div><script charset="utf-8" src="https://widgets.2gis.com/js/DGWidgetLoader.js"></script><script charset="utf-8">new DGWidgetLoader({"width":640,"height":600,"borderColor":"#a3a3a3","pos":{"lat":42.845011,"lon":74.587426,"zoom":16},"opt":{"city":"bishkek"},"org":[{"id":"70000001021088130"}]});</script><noscript style="color:#c00;font-size:16px;font-weight:bold;">Виджет карты использует JavaScript. Включите его в настройках вашего браузера.</noscript>
    ''')

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'


class Product(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    mini_description = RichTextField(verbose_name='Мини Описание', blank=True, null=True)
    price = models.CharField(max_length=123, verbose_name='Цена')
    image1 = models.ImageField(upload_to='images/products/', verbose_name='Изображение')
    image2 = models.ImageField(upload_to='images/products/', verbose_name='Изображение', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/products/', verbose_name='Изображение', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/products/', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    year = models.CharField(max_length=123, blank=True, null=True, verbose_name='Год')
    type = models.CharField(max_length=123, blank=True, null=True, verbose_name='Тип')
    make = models.CharField(max_length=123, blank=True, null=True, verbose_name='Производитель')
    engine_type = models.CharField(max_length=123, blank=True, null=True, verbose_name='Тип двигателя')
    engine_power = models.CharField(max_length=123, blank=True, null=True, verbose_name='Мощность двигателя')
    displacement = models.CharField(max_length=123, blank=True, null=True, verbose_name='Объем двигателя')
    bore_stroke = models.CharField(max_length=123, blank=True, null=True, verbose_name='Диаметр и ход поршня')
    size = models.CharField(max_length=123, blank=True, null=True, verbose_name='Размер')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class Industry(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'


class Application(models.Model):
    first_name = models.CharField(max_length=123, verbose_name='Имя')
    phone = models.CharField(max_length=123, verbose_name='Номер телефона')
    email = models.EmailField(max_length=123, verbose_name='Почта')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Товар', blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, verbose_name='индустрия', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заявка от {self.first_name}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class CategoryVacancy(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория для вакансий'
        verbose_name_plural = 'Категории для вакансий'
        ordering = ['-created_at']


class Vacancy(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    mini_description = models.CharField(max_length=123, verbose_name='мини название')
    description = RichTextField(verbose_name='Описание')
    category = models.ForeignKey(CategoryVacancy, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_at']


class SiteContent(models.Model):
    original_text = models.TextField(verbose_name="Оригинальный текст",
                                     help_text="Оригинальный текст, который отображается на сайте.",
                                     max_length=20000
                                     )
    current_text = models.TextField(
        verbose_name="Текущий текст",
        help_text="Измененный или текущий текст, который отображается на сайте.",
        max_length=20000
    )

    class Meta:
        verbose_name = "Контент сайта"
        verbose_name_plural = "Контент сайта"


class AboutImages(models.Model):
    title = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Изображение о нас'
