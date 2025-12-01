# Users

Types:

```python
from james_burvel_ocallaghan_iii.types import Address, User, UserLoginResponse
```

Methods:

- <code title="post /users/login">client.users.<a href="./src/james_burvel_ocallaghan_iii/resources/users/users.py">login</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/user_login_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/user_login_response.py">UserLoginResponse</a></code>
- <code title="post /users/register">client.users.<a href="./src/james_burvel_ocallaghan_iii/resources/users/users.py">register</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/user_register_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/user.py">User</a></code>

## PasswordReset

Types:

```python
from james_burvel_ocallaghan_iii.types.users import (
    PasswordResetConfirmResponse,
    PasswordResetInitiateResponse,
)
```

Methods:

- <code title="post /users/password-reset/confirm">client.users.password_reset.<a href="./src/james_burvel_ocallaghan_iii/resources/users/password_reset.py">confirm</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/password_reset_confirm_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/password_reset_confirm_response.py">PasswordResetConfirmResponse</a></code>
- <code title="post /users/password-reset/initiate">client.users.password_reset.<a href="./src/james_burvel_ocallaghan_iii/resources/users/password_reset.py">initiate</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/password_reset_initiate_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/password_reset_initiate_response.py">PasswordResetInitiateResponse</a></code>

## Me

Methods:

- <code title="get /users/me">client.users.me.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/me.py">retrieve</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/user.py">User</a></code>
- <code title="put /users/me">client.users.me.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/me.py">update</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/me_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/user.py">User</a></code>

### Preferences

Types:

```python
from james_burvel_ocallaghan_iii.types.users.me import (
    UserPreferences,
    UserPreferencesNotificationChannels,
)
```

Methods:

- <code title="get /users/me/preferences">client.users.me.preferences.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/preferences.py">retrieve</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/user_preferences.py">UserPreferences</a></code>
- <code title="put /users/me/preferences">client.users.me.preferences.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/preferences.py">update</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/me/preference_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/user_preferences.py">UserPreferences</a></code>

### Devices

Types:

```python
from james_burvel_ocallaghan_iii.types.users.me import Device, DeviceListResponse
```

Methods:

- <code title="get /users/me/devices">client.users.me.devices.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/devices.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/me/device_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/device_list_response.py">DeviceListResponse</a></code>
- <code title="delete /users/me/devices/{deviceId}">client.users.me.devices.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/devices.py">deregister</a>(device_id) -> None</code>
- <code title="post /users/me/devices">client.users.me.devices.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/devices.py">register</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/me/device_register_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/device.py">Device</a></code>

### Biometrics

Types:

```python
from james_burvel_ocallaghan_iii.types.users.me import BiometricStatus, BiometricVerifyResponse
```

Methods:

- <code title="delete /users/me/biometrics">client.users.me.biometrics.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/biometrics.py">deregister</a>() -> None</code>
- <code title="post /users/me/biometrics/enroll">client.users.me.biometrics.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/biometrics.py">enroll</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/me/biometric_enroll_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/biometric_status.py">BiometricStatus</a></code>
- <code title="get /users/me/biometrics">client.users.me.biometrics.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/biometrics.py">status</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/biometric_status.py">BiometricStatus</a></code>
- <code title="post /users/me/biometrics/verify">client.users.me.biometrics.<a href="./src/james_burvel_ocallaghan_iii/resources/users/me/biometrics.py">verify</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/users/me/biometric_verify_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/users/me/biometric_verify_response.py">BiometricVerifyResponse</a></code>

# Accounts

Types:

```python
from james_burvel_ocallaghan_iii.types import (
    LinkedAccount,
    AccountLinkNewInstitutionResponse,
    AccountListLinkedAccountsResponse,
    AccountRetrieveAccountDetailsResponse,
    AccountRetrieveAccountStatementsResponse,
)
```

Methods:

- <code title="post /accounts/link">client.accounts.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/accounts.py">link_new_institution</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/account_link_new_institution_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/account_link_new_institution_response.py">AccountLinkNewInstitutionResponse</a></code>
- <code title="get /accounts/me">client.accounts.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/accounts.py">list_linked_accounts</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/account_list_linked_accounts_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/account_list_linked_accounts_response.py">AccountListLinkedAccountsResponse</a></code>
- <code title="get /accounts/{accountId}/details">client.accounts.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/accounts.py">retrieve_account_details</a>(account_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/account_retrieve_account_details_response.py">AccountRetrieveAccountDetailsResponse</a></code>
- <code title="get /accounts/{accountId}/statements">client.accounts.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/accounts.py">retrieve_account_statements</a>(account_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/account_retrieve_account_statements_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/account_retrieve_account_statements_response.py">AccountRetrieveAccountStatementsResponse</a></code>

## Transactions

Types:

```python
from james_burvel_ocallaghan_iii.types.accounts import TransactionListPendingTransactionsResponse
```

Methods:

- <code title="get /accounts/{accountId}/transactions/pending">client.accounts.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/transactions.py">list_pending_transactions</a>(account_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/accounts/transaction_list_pending_transactions_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/accounts/transaction_list_pending_transactions_response.py">TransactionListPendingTransactionsResponse</a></code>

## OverdraftSettings

Types:

```python
from james_burvel_ocallaghan_iii.types.accounts import OverdraftSettings
```

Methods:

- <code title="get /accounts/{accountId}/overdraft-settings">client.accounts.overdraft_settings.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/overdraft_settings.py">retrieve_settings</a>(account_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/accounts/overdraft_settings.py">OverdraftSettings</a></code>
- <code title="put /accounts/{accountId}/overdraft-settings">client.accounts.overdraft_settings.<a href="./src/james_burvel_ocallaghan_iii/resources/accounts/overdraft_settings.py">update_settings</a>(account_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/accounts/overdraft_setting_update_settings_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/accounts/overdraft_settings.py">OverdraftSettings</a></code>

# Transactions

Types:

```python
from james_burvel_ocallaghan_iii.types import (
    PaginatedTransactions,
    Transaction,
    TransactionDisputeResponse,
)
```

Methods:

- <code title="get /transactions/{transactionId}">client.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/transactions.py">retrieve</a>(transaction_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/transaction.py">Transaction</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/transactions.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/transaction_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/paginated_transactions.py">PaginatedTransactions</a></code>
- <code title="put /transactions/{transactionId}/categorize">client.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/transactions.py">categorize</a>(transaction_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/transaction_categorize_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/transaction.py">Transaction</a></code>
- <code title="post /transactions/{transactionId}/dispute">client.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/transactions.py">dispute</a>(transaction_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/transaction_dispute_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/transaction_dispute_response.py">TransactionDisputeResponse</a></code>
- <code title="put /transactions/{transactionId}/notes">client.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/transactions.py">update_notes</a>(transaction_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/transaction_update_notes_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/transaction.py">Transaction</a></code>

## Recurring

Types:

```python
from james_burvel_ocallaghan_iii.types.transactions import (
    RecurringTransaction,
    RecurringListResponse,
)
```

Methods:

- <code title="post /transactions/recurring">client.transactions.recurring.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/recurring.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/transactions/recurring_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/transactions/recurring_transaction.py">RecurringTransaction</a></code>
- <code title="get /transactions/recurring">client.transactions.recurring.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/recurring.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/transactions/recurring_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/transactions/recurring_list_response.py">RecurringListResponse</a></code>

## Insights

Types:

```python
from james_burvel_ocallaghan_iii.types.transactions import (
    AIInsight,
    InsightGetSpendingTrendsResponse,
)
```

Methods:

- <code title="get /transactions/insights/spending-trends">client.transactions.insights.<a href="./src/james_burvel_ocallaghan_iii/resources/transactions/insights.py">get_spending_trends</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/transactions/insight_get_spending_trends_response.py">InsightGetSpendingTrendsResponse</a></code>

# Budgets

Types:

```python
from james_burvel_ocallaghan_iii.types import Budget, BudgetListResponse
```

Methods:

- <code title="post /budgets">client.budgets.<a href="./src/james_burvel_ocallaghan_iii/resources/budgets.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/budget_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/budget.py">Budget</a></code>
- <code title="get /budgets/{budgetId}">client.budgets.<a href="./src/james_burvel_ocallaghan_iii/resources/budgets.py">retrieve</a>(budget_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/budget.py">Budget</a></code>
- <code title="put /budgets/{budgetId}">client.budgets.<a href="./src/james_burvel_ocallaghan_iii/resources/budgets.py">update</a>(budget_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/budget_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/budget.py">Budget</a></code>
- <code title="get /budgets">client.budgets.<a href="./src/james_burvel_ocallaghan_iii/resources/budgets.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/budget_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/budget_list_response.py">BudgetListResponse</a></code>
- <code title="delete /budgets/{budgetId}">client.budgets.<a href="./src/james_burvel_ocallaghan_iii/resources/budgets.py">delete</a>(budget_id) -> None</code>

# Investments

## Portfolios

Types:

```python
from james_burvel_ocallaghan_iii.types.investments import (
    InvestmentPortfolio,
    PortfolioListResponse,
    PortfolioRebalanceResponse,
)
```

Methods:

- <code title="post /investments/portfolios">client.investments.portfolios.<a href="./src/james_burvel_ocallaghan_iii/resources/investments/portfolios.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/investments/portfolio_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/investments/investment_portfolio.py">InvestmentPortfolio</a></code>
- <code title="get /investments/portfolios/{portfolioId}">client.investments.portfolios.<a href="./src/james_burvel_ocallaghan_iii/resources/investments/portfolios.py">retrieve</a>(portfolio_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/investments/investment_portfolio.py">InvestmentPortfolio</a></code>
- <code title="put /investments/portfolios/{portfolioId}">client.investments.portfolios.<a href="./src/james_burvel_ocallaghan_iii/resources/investments/portfolios.py">update</a>(portfolio_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/investments/portfolio_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/investments/investment_portfolio.py">InvestmentPortfolio</a></code>
- <code title="get /investments/portfolios">client.investments.portfolios.<a href="./src/james_burvel_ocallaghan_iii/resources/investments/portfolios.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/investments/portfolio_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/investments/portfolio_list_response.py">PortfolioListResponse</a></code>
- <code title="post /investments/portfolios/{portfolioId}/rebalance">client.investments.portfolios.<a href="./src/james_burvel_ocallaghan_iii/resources/investments/portfolios.py">rebalance</a>(portfolio_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/investments/portfolio_rebalance_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/investments/portfolio_rebalance_response.py">PortfolioRebalanceResponse</a></code>

## Assets

Types:

```python
from james_burvel_ocallaghan_iii.types.investments import AssetSearchResponse
```

Methods:

- <code title="get /investments/assets/search">client.investments.assets.<a href="./src/james_burvel_ocallaghan_iii/resources/investments/assets.py">search</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/investments/asset_search_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/investments/asset_search_response.py">AssetSearchResponse</a></code>

# AI

## Advisor

Types:

```python
from james_burvel_ocallaghan_iii.types.ai import AdvisorListToolsResponse
```

Methods:

- <code title="get /ai/advisor/tools">client.ai.advisor.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/advisor/advisor.py">list_tools</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/advisor_list_tools_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/advisor_list_tools_response.py">AdvisorListToolsResponse</a></code>

### Chat

Types:

```python
from james_burvel_ocallaghan_iii.types.ai.advisor import (
    ChatRetrieveHistoryResponse,
    ChatSendMessageResponse,
)
```

Methods:

- <code title="get /ai/advisor/chat/history">client.ai.advisor.chat.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/advisor/chat.py">retrieve_history</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/advisor/chat_retrieve_history_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/advisor/chat_retrieve_history_response.py">ChatRetrieveHistoryResponse</a></code>
- <code title="post /ai/advisor/chat">client.ai.advisor.chat.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/advisor/chat.py">send_message</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/advisor/chat_send_message_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/advisor/chat_send_message_response.py">ChatSendMessageResponse</a></code>

## Oracle

### Simulate

Types:

```python
from james_burvel_ocallaghan_iii.types.ai.oracle import (
    AdvancedSimulationResponse,
    SimulationResponse,
)
```

Methods:

- <code title="post /ai/oracle/simulate/advanced">client.ai.oracle.simulate.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/oracle/simulate.py">run_advanced</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/oracle/simulate_run_advanced_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/oracle/advanced_simulation_response.py">AdvancedSimulationResponse</a></code>
- <code title="post /ai/oracle/simulate">client.ai.oracle.simulate.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/oracle/simulate.py">run_standard</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/oracle/simulate_run_standard_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/oracle/simulation_response.py">SimulationResponse</a></code>

### Simulations

Types:

```python
from james_burvel_ocallaghan_iii.types.ai.oracle import (
    SimulationRetrieveResponse,
    SimulationListResponse,
)
```

Methods:

- <code title="get /ai/oracle/simulations/{simulationId}">client.ai.oracle.simulations.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/oracle/simulations.py">retrieve</a>(simulation_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/oracle/simulation_retrieve_response.py">SimulationRetrieveResponse</a></code>
- <code title="get /ai/oracle/simulations">client.ai.oracle.simulations.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/oracle/simulations.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/oracle/simulation_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/oracle/simulation_list_response.py">SimulationListResponse</a></code>
- <code title="delete /ai/oracle/simulations/{simulationId}">client.ai.oracle.simulations.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/oracle/simulations.py">delete</a>(simulation_id) -> None</code>

## Incubator

Types:

```python
from james_burvel_ocallaghan_iii.types.ai import IncubatorListPitchesResponse
```

Methods:

- <code title="get /ai/incubator/pitches">client.ai.incubator.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/incubator/incubator.py">list_pitches</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/incubator_list_pitches_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/incubator_list_pitches_response.py">IncubatorListPitchesResponse</a></code>

### Pitch

Types:

```python
from james_burvel_ocallaghan_iii.types.ai.incubator import (
    QuantumWeaverState,
    PitchRetrieveDetailsResponse,
)
```

Methods:

- <code title="get /ai/incubator/pitch/{pitchId}/details">client.ai.incubator.pitch.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/incubator/pitch.py">retrieve_details</a>(pitch_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/incubator/pitch_retrieve_details_response.py">PitchRetrieveDetailsResponse</a></code>
- <code title="post /ai/incubator/pitch">client.ai.incubator.pitch.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/incubator/pitch.py">submit</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/incubator/pitch_submit_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/incubator/quantum_weaver_state.py">QuantumWeaverState</a></code>
- <code title="put /ai/incubator/pitch/{pitchId}/feedback">client.ai.incubator.pitch.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/incubator/pitch.py">submit_feedback</a>(pitch_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/incubator/pitch_submit_feedback_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/incubator/quantum_weaver_state.py">QuantumWeaverState</a></code>

## Ads

Types:

```python
from james_burvel_ocallaghan_iii.types.ai import VideoOperationStatus, AdListGeneratedResponse
```

Methods:

- <code title="get /ai/ads">client.ai.ads.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/ads/ads.py">list_generated</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/ad_list_generated_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/ad_list_generated_response.py">AdListGeneratedResponse</a></code>
- <code title="get /ai/ads/operations/{operationId}">client.ai.ads.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/ads/ads.py">retrieve_status</a>(operation_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/video_operation_status.py">VideoOperationStatus</a></code>

### Generate

Types:

```python
from james_burvel_ocallaghan_iii.types.ai.ads import (
    GenerateVideoRequest,
    GenerateAdvancedResponse,
    GenerateStandardResponse,
)
```

Methods:

- <code title="post /ai/ads/generate/advanced">client.ai.ads.generate.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/ads/generate.py">advanced</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/ads/generate_advanced_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/ads/generate_advanced_response.py">GenerateAdvancedResponse</a></code>
- <code title="post /ai/ads/generate">client.ai.ads.generate.<a href="./src/james_burvel_ocallaghan_iii/resources/ai/ads/generate.py">standard</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/ai/ads/generate_standard_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/ai/ads/generate_standard_response.py">GenerateStandardResponse</a></code>

# Corporate

Types:

```python
from james_burvel_ocallaghan_iii.types import CorporatePerformSanctionScreeningResponse
```

Methods:

- <code title="post /corporate/sanction-screening">client.corporate.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/corporate.py">perform_sanction_screening</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate_perform_sanction_screening_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate_perform_sanction_screening_response.py">CorporatePerformSanctionScreeningResponse</a></code>

## Cards

Types:

```python
from james_burvel_ocallaghan_iii.types.corporate import (
    CorporateCard,
    CorporateCardControls,
    CardListResponse,
)
```

Methods:

- <code title="get /corporate/cards">client.corporate.cards.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/cards.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/card_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/card_list_response.py">CardListResponse</a></code>
- <code title="post /corporate/cards/virtual">client.corporate.cards.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/cards.py">create_virtual</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/card_create_virtual_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/corporate_card.py">CorporateCard</a></code>
- <code title="post /corporate/cards/{cardId}/freeze">client.corporate.cards.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/cards.py">freeze</a>(card_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/card_freeze_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/corporate_card.py">CorporateCard</a></code>
- <code title="get /corporate/cards/{cardId}/transactions">client.corporate.cards.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/cards.py">list_transactions</a>(card_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/card_list_transactions_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/paginated_transactions.py">PaginatedTransactions</a></code>
- <code title="put /corporate/cards/{cardId}/controls">client.corporate.cards.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/cards.py">update_controls</a>(card_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/card_update_controls_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/corporate_card.py">CorporateCard</a></code>

## Anomalies

Types:

```python
from james_burvel_ocallaghan_iii.types.corporate import FinancialAnomaly, AnomalyListResponse
```

Methods:

- <code title="get /corporate/anomalies">client.corporate.anomalies.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/anomalies.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/anomaly_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/anomaly_list_response.py">AnomalyListResponse</a></code>
- <code title="put /corporate/anomalies/{anomalyId}/status">client.corporate.anomalies.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/anomalies.py">update_status</a>(anomaly_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/anomaly_update_status_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/financial_anomaly.py">FinancialAnomaly</a></code>

## Compliance

### Audits

Types:

```python
from james_burvel_ocallaghan_iii.types.corporate.compliance import (
    AuditRequestResponse,
    AuditRetrieveReportResponse,
)
```

Methods:

- <code title="post /corporate/compliance/audits">client.corporate.compliance.audits.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/compliance/audits.py">request</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/compliance/audit_request_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/compliance/audit_request_response.py">AuditRequestResponse</a></code>
- <code title="get /corporate/compliance/audits/{auditId}/report">client.corporate.compliance.audits.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/compliance/audits.py">retrieve_report</a>(audit_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/compliance/audit_retrieve_report_response.py">AuditRetrieveReportResponse</a></code>

## Treasury

Types:

```python
from james_burvel_ocallaghan_iii.types.corporate import TreasuryGetLiquidityPositionsResponse
```

Methods:

- <code title="get /corporate/treasury/liquidity-positions">client.corporate.treasury.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/treasury/treasury.py">get_liquidity_positions</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/treasury_get_liquidity_positions_response.py">TreasuryGetLiquidityPositionsResponse</a></code>

### CashFlow

Types:

```python
from james_burvel_ocallaghan_iii.types.corporate.treasury import CashFlowForecastResponse
```

Methods:

- <code title="get /corporate/treasury/cash-flow/forecast">client.corporate.treasury.cash_flow.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/treasury/cash_flow.py">forecast</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/treasury/cash_flow_forecast_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/treasury/cash_flow_forecast_response.py">CashFlowForecastResponse</a></code>

## Risk

### Fraud

#### Rules

Types:

```python
from james_burvel_ocallaghan_iii.types.corporate.risk.fraud import (
    FraudRule,
    FraudRuleAction,
    FraudRuleCriteria,
    RuleListResponse,
)
```

Methods:

- <code title="post /corporate/risk/fraud/rules">client.corporate.risk.fraud.rules.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/risk/fraud/rules.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/risk/fraud/rule_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/risk/fraud/fraud_rule.py">FraudRule</a></code>
- <code title="put /corporate/risk/fraud/rules/{ruleId}">client.corporate.risk.fraud.rules.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/risk/fraud/rules.py">update</a>(rule_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/risk/fraud/rule_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/risk/fraud/fraud_rule.py">FraudRule</a></code>
- <code title="get /corporate/risk/fraud/rules">client.corporate.risk.fraud.rules.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/risk/fraud/rules.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/corporate/risk/fraud/rule_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/corporate/risk/fraud/rule_list_response.py">RuleListResponse</a></code>
- <code title="delete /corporate/risk/fraud/rules/{ruleId}">client.corporate.risk.fraud.rules.<a href="./src/james_burvel_ocallaghan_iii/resources/corporate/risk/fraud/rules.py">delete</a>(rule_id) -> None</code>

# Web3

Types:

```python
from james_burvel_ocallaghan_iii.types import Web3RetrieveNFTsResponse
```

Methods:

- <code title="get /web3/nfts">client.web3.<a href="./src/james_burvel_ocallaghan_iii/resources/web3/web3.py">retrieve_nfts</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/web3_retrieve_nfts_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/web3_retrieve_nfts_response.py">Web3RetrieveNFTsResponse</a></code>

## Wallets

Types:

```python
from james_burvel_ocallaghan_iii.types.web3 import (
    CryptoWalletConnection,
    WalletListResponse,
    WalletRetrieveBalancesResponse,
)
```

Methods:

- <code title="get /web3/wallets">client.web3.wallets.<a href="./src/james_burvel_ocallaghan_iii/resources/web3/wallets.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/web3/wallet_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/web3/wallet_list_response.py">WalletListResponse</a></code>
- <code title="post /web3/wallets">client.web3.wallets.<a href="./src/james_burvel_ocallaghan_iii/resources/web3/wallets.py">connect</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/web3/wallet_connect_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/web3/crypto_wallet_connection.py">CryptoWalletConnection</a></code>
- <code title="get /web3/wallets/{walletId}/balances">client.web3.wallets.<a href="./src/james_burvel_ocallaghan_iii/resources/web3/wallets.py">retrieve_balances</a>(wallet_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/web3/wallet_retrieve_balances_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/web3/wallet_retrieve_balances_response.py">WalletRetrieveBalancesResponse</a></code>

## Transactions

Types:

```python
from james_burvel_ocallaghan_iii.types.web3 import TransactionInitiateTransferResponse
```

Methods:

- <code title="post /web3/transactions/initiate">client.web3.transactions.<a href="./src/james_burvel_ocallaghan_iii/resources/web3/transactions.py">initiate_transfer</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/web3/transaction_initiate_transfer_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/web3/transaction_initiate_transfer_response.py">TransactionInitiateTransferResponse</a></code>

# Payments

## International

Types:

```python
from james_burvel_ocallaghan_iii.types.payments import InternationalPaymentStatus
```

Methods:

- <code title="post /payments/international/initiate">client.payments.international.<a href="./src/james_burvel_ocallaghan_iii/resources/payments/international.py">initiate</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/payments/international_initiate_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/payments/international_payment_status.py">InternationalPaymentStatus</a></code>
- <code title="get /payments/international/{paymentId}/status">client.payments.international.<a href="./src/james_burvel_ocallaghan_iii/resources/payments/international.py">retrieve_status</a>(payment_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/payments/international_payment_status.py">InternationalPaymentStatus</a></code>

## Fx

Types:

```python
from james_burvel_ocallaghan_iii.types.payments import FxConvertResponse, FxRetrieveRatesResponse
```

Methods:

- <code title="post /payments/fx/convert">client.payments.fx.<a href="./src/james_burvel_ocallaghan_iii/resources/payments/fx.py">convert</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/payments/fx_convert_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/payments/fx_convert_response.py">FxConvertResponse</a></code>
- <code title="get /payments/fx/rates">client.payments.fx.<a href="./src/james_burvel_ocallaghan_iii/resources/payments/fx.py">retrieve_rates</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/payments/fx_retrieve_rates_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/payments/fx_retrieve_rates_response.py">FxRetrieveRatesResponse</a></code>

# Sustainability

Types:

```python
from james_burvel_ocallaghan_iii.types import (
    SustainabilityPurchaseCarbonOffsetsResponse,
    SustainabilityRetrieveCarbonFootprintResponse,
)
```

Methods:

- <code title="post /sustainability/carbon-offsets">client.sustainability.<a href="./src/james_burvel_ocallaghan_iii/resources/sustainability/sustainability.py">purchase_carbon_offsets</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/sustainability_purchase_carbon_offsets_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/sustainability_purchase_carbon_offsets_response.py">SustainabilityPurchaseCarbonOffsetsResponse</a></code>
- <code title="get /sustainability/carbon-footprint">client.sustainability.<a href="./src/james_burvel_ocallaghan_iii/resources/sustainability/sustainability.py">retrieve_carbon_footprint</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/sustainability_retrieve_carbon_footprint_response.py">SustainabilityRetrieveCarbonFootprintResponse</a></code>

## Investments

Types:

```python
from james_burvel_ocallaghan_iii.types.sustainability import InvestmentAnalyzeImpactResponse
```

Methods:

- <code title="get /sustainability/investments/impact">client.sustainability.investments.<a href="./src/james_burvel_ocallaghan_iii/resources/sustainability/investments.py">analyze_impact</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/sustainability/investment_analyze_impact_response.py">InvestmentAnalyzeImpactResponse</a></code>

# Lending

## Applications

Types:

```python
from james_burvel_ocallaghan_iii.types.lending import LoanApplicationStatus
```

Methods:

- <code title="get /lending/applications/{applicationId}">client.lending.applications.<a href="./src/james_burvel_ocallaghan_iii/resources/lending/applications.py">retrieve</a>(application_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/lending/loan_application_status.py">LoanApplicationStatus</a></code>
- <code title="post /lending/applications">client.lending.applications.<a href="./src/james_burvel_ocallaghan_iii/resources/lending/applications.py">submit</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/lending/application_submit_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/lending/loan_application_status.py">LoanApplicationStatus</a></code>

## Offers

Types:

```python
from james_burvel_ocallaghan_iii.types.lending import LoanOffer, OfferListPreApprovedResponse
```

Methods:

- <code title="get /lending/offers/pre-approved">client.lending.offers.<a href="./src/james_burvel_ocallaghan_iii/resources/lending/offers.py">list_pre_approved</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/lending/offer_list_pre_approved_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/lending/offer_list_pre_approved_response.py">OfferListPreApprovedResponse</a></code>

# Developers

## Webhooks

Types:

```python
from james_burvel_ocallaghan_iii.types.developers import WebhookSubscription, WebhookListResponse
```

Methods:

- <code title="post /developers/webhooks">client.developers.webhooks.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/webhooks.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/developers/webhook_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/developers/webhook_subscription.py">WebhookSubscription</a></code>
- <code title="put /developers/webhooks/{subscriptionId}">client.developers.webhooks.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/webhooks.py">update</a>(subscription_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/developers/webhook_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/developers/webhook_subscription.py">WebhookSubscription</a></code>
- <code title="get /developers/webhooks">client.developers.webhooks.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/webhooks.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/developers/webhook_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/developers/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /developers/webhooks/{subscriptionId}">client.developers.webhooks.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/webhooks.py">delete</a>(subscription_id) -> None</code>

## APIKeys

Types:

```python
from james_burvel_ocallaghan_iii.types.developers import APIKey, APIKeyListResponse
```

Methods:

- <code title="post /developers/api-keys">client.developers.api_keys.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/api_keys.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/developers/api_key_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/developers/api_key.py">APIKey</a></code>
- <code title="get /developers/api-keys">client.developers.api_keys.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/api_keys.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/developers/api_key_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/developers/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /developers/api-keys/{keyId}">client.developers.api_keys.<a href="./src/james_burvel_ocallaghan_iii/resources/developers/api_keys.py">revoke</a>(key_id) -> None</code>

# Identity

## KYC

Types:

```python
from james_burvel_ocallaghan_iii.types.identity import KYCStatus
```

Methods:

- <code title="get /identity/kyc/status">client.identity.kyc.<a href="./src/james_burvel_ocallaghan_iii/resources/identity/kyc.py">retrieve_status</a>() -> <a href="./src/james_burvel_ocallaghan_iii/types/identity/kyc_status.py">KYCStatus</a></code>
- <code title="post /identity/kyc/submit">client.identity.kyc.<a href="./src/james_burvel_ocallaghan_iii/resources/identity/kyc.py">submit</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/identity/kyc_submit_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/identity/kyc_status.py">KYCStatus</a></code>

# Goals

Types:

```python
from james_burvel_ocallaghan_iii.types import FinancialGoal, GoalListResponse
```

Methods:

- <code title="post /goals">client.goals.<a href="./src/james_burvel_ocallaghan_iii/resources/goals.py">create</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/goal_create_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/financial_goal.py">FinancialGoal</a></code>
- <code title="get /goals/{goalId}">client.goals.<a href="./src/james_burvel_ocallaghan_iii/resources/goals.py">retrieve</a>(goal_id) -> <a href="./src/james_burvel_ocallaghan_iii/types/financial_goal.py">FinancialGoal</a></code>
- <code title="put /goals/{goalId}">client.goals.<a href="./src/james_burvel_ocallaghan_iii/resources/goals.py">update</a>(goal_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/goal_update_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/financial_goal.py">FinancialGoal</a></code>
- <code title="get /goals">client.goals.<a href="./src/james_burvel_ocallaghan_iii/resources/goals.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/goal_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/goal_list_response.py">GoalListResponse</a></code>
- <code title="delete /goals/{goalId}">client.goals.<a href="./src/james_burvel_ocallaghan_iii/resources/goals.py">delete</a>(goal_id) -> None</code>

# Marketplace

## Products

Types:

```python
from james_burvel_ocallaghan_iii.types.marketplace import (
    ProductListResponse,
    ProductRedeemMarketplaceOfferResponse,
    ProductSimulatePurchaseResponse,
)
```

Methods:

- <code title="get /marketplace/products">client.marketplace.products.<a href="./src/james_burvel_ocallaghan_iii/resources/marketplace/products.py">list</a>(\*\*<a href="src/james_burvel_ocallaghan_iii/types/marketplace/product_list_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/marketplace/product_list_response.py">ProductListResponse</a></code>
- <code title="post /marketplace/offers/{offerId}/redeem">client.marketplace.products.<a href="./src/james_burvel_ocallaghan_iii/resources/marketplace/products.py">redeem_marketplace_offer</a>(offer_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/marketplace/product_redeem_marketplace_offer_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/marketplace/product_redeem_marketplace_offer_response.py">ProductRedeemMarketplaceOfferResponse</a></code>
- <code title="post /marketplace/products/{productId}/impact-simulate">client.marketplace.products.<a href="./src/james_burvel_ocallaghan_iii/resources/marketplace/products.py">simulate_purchase</a>(product_id, \*\*<a href="src/james_burvel_ocallaghan_iii/types/marketplace/product_simulate_purchase_params.py">params</a>) -> <a href="./src/james_burvel_ocallaghan_iii/types/marketplace/product_simulate_purchase_response.py">ProductSimulatePurchaseResponse</a></code>
