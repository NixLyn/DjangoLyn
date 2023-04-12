# Authentication Analysis #

## Potential Vulnerablities ##
### Add Post ###


'homepage/forms.py'

```
# ! In the PostForm/meta/widgets('author')
# ? There is a potentional bug, given that it uses js id values, 
# @ By opening the console in a browers, dev tools, 
# @ it is possible to change the value of this user_id before submitting

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'add_on', 'color')
        widgets = {
            'title':    forms.TextInput(attrs={'class': 'form-control',}),

            'author':   forms.Select(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
                # Here we assign some basics for the template ^         ^!^         ^^             ^^

            'body':     forms.Textarea(attrs={'class': 'form-control'}),
            'add_on':   forms.TextInput(attrs={'class': 'form-control'}),
            'color':    forms.Select(attrs={'class': 'form-control'}),
            }

```

'homepage/templates/add_post.html'

```
        ...
        {% if user.is_authenticated %}
            <h1>Add NoticeBoard Post</h1>
            <div class="form-group">
                <form method="POST">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <button>Post</button>
                </form>
            </div>
            <script>
                /* First we collect the ID of the current user */
                var user = "{{ user.id }}";
                /* Then assign it to the 'id_author' value */
                document.getElementById('id_author').value = user;
                /* We then collect the parentNode of the element */
                var p_val = document.querySelector('#id_author').parentNode;
                /* And hid the whole block */
                p_val.style.display = 'none'
                /* This Can be found in 'view source' and be edited via the console */
            </script>
        {% else %}
        ...
```
