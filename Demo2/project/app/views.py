from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name':'sam','marks':100},
        {'name':'sedly','marks':99},
        {'name':'itly','marks':88},
        {'name':'chintu','marks':90},
        {'name':'pintu','marks':92},
        {'name':'maddy','marks':56},
        {'name':'ram','marks':40}
    ]
    text = """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium, ab! Porro possimus, dicta eligendi fugit modi reiciendis sed temporibus maiores non suscipit atque ullam error tempora aperiam at ut doloremque.
        Aliquam et quam, soluta, facilis eos ratione, dolorem sunt quis velit illo hic ducimus error distinctio assumenda voluptates exercitationem sint rem dolor? Amet perspiciatis consectetur hic, expedita delectus laudantium cum!
        Tempora accusantium, culpa optio itaque temporibus earum quidem quisquam non similique, iusto, corporis ab officiis repellat delectus laudantium sapiente blanditiis at molestias mollitia! Reprehenderit, assumenda rerum hic quod consequatur dolores?
        Dignissimos nobis impedit sunt excepturi quo mollitia voluptas. Perspiciatis quis quaerat sunt? Delectus accusamus quidem, corporis incidunt beatae eaque perferendis doloremque error provident, voluptatem aliquid recusandae at quia, labore saepe?
        Atque repellat reiciendis rem harum culpa officia dolores recusandae! Eum perspiciatis accusantium tenetur, repellat vel nihil? Facilis similique beatae neque, quo dignissimos perferendis quae autem porro est. Rem, ex iure!
        Ipsum, soluta. Eum, quae numquam velit quo neque soluta. Quia ullam, totam dolorum voluptatem dolores quidem architecto similique temporibus possimus debitis id cupiditate corporis, eum dolorem nisi itaque rerum nemo!
        Aliquam perferendis cumque natus eos nobis debitis maxime quia mollitia velit sequi in quis accusantium aliquid, laudantium, libero quisquam consequatur suscipit explicabo a deserunt nemo ratione omnis dolore. Perspiciatis, quibusdam.
        Similique ea rem quas voluptatibus culpa, laboriosam hic eaque tenetur eos temporibus distinctio optio quae eligendi in dolores odit placeat incidunt mollitia error saepe doloremque. Molestiae, amet. Laborum, tenetur minima?
        Nostrum, eius! Autem repellat veritatis soluta consequatur fuga laboriosam aspernatur ducimus ad voluptate aliquid pariatur commodi, maxime blanditiis eius quibusdam deleniti, provident quos aperiam nisi quo similique omnis numquam consectetur.
        Blanditiis laboriosam voluptatum molestiae reprehenderit autem nostrum tempore aliquid exercitationem assumenda, harum perspiciatis id molestias dolore earum? Aliquid rerum consectetur dolorem excepturi omnis doloribus autem obcaecati, quia neque, natus sed.
    """
    context = {'peoples':peoples,'text':text,'page':'home'}
    return render(request,'index.html',context)

def contact(request):
    context = {'page':'contact'}
    return render(request,'contact.html',context)

def about(request):
    context = {'page':'about'}
    return render(request,'about.html',context)