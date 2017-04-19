'''
* `prestige` _(From yesterday afternoon)_
    - Prediction of the prestige of a job
    - Dependent variable: `prestige`
    - Independent variables: `income`, `education`'''

prestige = sm.datasets.get_rdataset("Duncan", "car", cache=True).data
y = prestige['prestige']
x = prestige[['income', 'education']].astype(float)
x = sm.add_constant(x)
num_vars=['income', 'education']
features = np.array(x)
target = np.array(y)

'''
* `ccard`
    - Prediction of the average credit card expenditure
    - Dependent variable: `AVGEXP`
    - Independent variables: `AGE`, `INCOME`, `INCOMESQ` (`INCOME^2`), `OWNRENT`
'''
credit_card = sm.datasets.ccard.load_pandas().data


def prestige_scater():
    fig, ax=plt.subplots(1,1,figsize=(10,10))
    num_vars=['income', 'education']
    ax = scatter_matrix(prestige[num_vars], ax=ax, diagonal='kde')
    plt.show()
    plt.savefig('scatter_matrix.png')

def prestige_box():
    fig, axes=plt.subplots(1,2,figsize=(10,10))
    for ax, var in zip(axes.ravel(), num_vars):
        ax.boxplot(prestige[var])
        ax.set_title(var)
    plt.tight_layout()

def linear_model():
    beta = np.dot(np.dot(np.linalg.inv(np.dot(features.T,features)),features.T),target)
    return beta

def ols():
    model = sms.OLS(target, features).fit()
    summary = model.summary()
    return summary
