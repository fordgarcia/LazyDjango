# Workflow

configuration are text files that houses paths :)
current command:  python -m lazydjango.module.initialize

1. Non-flag
    * d, default
        * ask for build path (absolute)
            * build default
    * u, user
        * show user configurations
            * ask for build path (absolute)
                * build chosen configuration
            * cancel
    * o, other
        * show current directory configurations
            * build chosen configuration
        * cancel
2. Flag
    * -d, --default
    * -c, --custom 
    * -s, --set_default
    * -h, --help