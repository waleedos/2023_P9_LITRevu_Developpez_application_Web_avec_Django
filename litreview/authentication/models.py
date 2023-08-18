# Powered By M. EL-WALID EL-KHABOU

from django.contrib.auth.models import AbstractUser
# Importation de AbstractUser : Nous importons la classe AbstractUser du module django.contrib.auth.models. AbstractUser
# est une classe abstraite fournie par Django qui contient tous les champs et méthodes nécessaires pour gérer
# l'authentification et l'autorisation des utilisateurs. En utilisant cette classe comme base, vous pouvez facilement
# étendre ou personnaliser le modèle utilisateur par défaut fourni par Django.


class User(AbstractUser):
    # Définition de la classe User : Nous définissons une classe User qui hérite de AbstractUser. En faisant cela, notre
    # modèle User hérite de tous les champs et méthodes de AbstractUser, ce qui le rend compatible avec le système
    # d'authentification intégré de Django. Cela signifie également que Nous pouvons ajouter des champs supplémentaires à ce
    # modèle à l'avenir si nous en avons besoin, sans avoir à redéfinir tout le modèle utilisateur.

    # Utilisation de la méthode __str__ qui est une représentation sous forme de chaîne du modèle. Lorsqu'une instance
    # du modèle User est convertie en chaîne (par exemple, pour l'affichage dans l'interface d'administration de Django),
    # cette méthode retourne le nom d'utilisateur de l'instance. C'est utile pour avoir une représentation lisible d'une
    # instance du modèle.
    def __str__(self):
        return self.username
