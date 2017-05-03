# teamcity-webgui-wrapper

Workaround for https://youtrack.jetbrains.com/issue/TW-21447

[![teamcity-webgui-wrapper code quality](https://api.codacy.com/project/badge/Grade/233da50a5d4744ef8918ed15fbfc0eba)](https://www.codacy.com/app/tim55667757/teamcity-webgui-wrapper/dashboard)

## Functional
1. Move Configuration to other Project
2. That's all for now :)

## Usage
``` python
from TeamcityWebGui import TeamcityWebGui

teamcityGui = TeamcityWebGui("https://teamcity.example.com", user, password)
teamcityGui.moveBuildType('MyConfigurationId', 'ToMyProjectId')
```

### Requirements
- Firefox
- pypi modules in requirements.txt
