# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

require 'uri'
require 'cgi'
require 'date'
require 'json'
require 'base64'
require 'erb'
require 'securerandom'
require 'time'
require 'timeliness'
require 'faraday'
require 'faraday-cookie_jar'
require 'concurrent'
require 'ms_rest'
require 'generated/azure_mgmt_subscriptions/module_definition'
require 'generated/azure_mgmt_subscriptions/version'
require 'ms_rest_azure'

module Azure::ARM::Subscriptions
  autoload :Subscriptions,                                      'generated/azure_mgmt_subscriptions/subscriptions.rb'
  autoload :Tenants,                                            'generated/azure_mgmt_subscriptions/tenants.rb'
  autoload :SubscriptionClient,                                 'generated/azure_mgmt_subscriptions/subscription_client.rb'

  module Models
    autoload :Location,                                           'generated/azure_mgmt_subscriptions/models/location.rb'
    autoload :LocationListResult,                                 'generated/azure_mgmt_subscriptions/models/location_list_result.rb'
    autoload :Subscription,                                       'generated/azure_mgmt_subscriptions/models/subscription.rb'
    autoload :SubscriptionPolicies,                               'generated/azure_mgmt_subscriptions/models/subscription_policies.rb'
    autoload :SubscriptionListResult,                             'generated/azure_mgmt_subscriptions/models/subscription_list_result.rb'
    autoload :TenantIdDescription,                                'generated/azure_mgmt_subscriptions/models/tenant_id_description.rb'
    autoload :TenantListResult,                                   'generated/azure_mgmt_subscriptions/models/tenant_list_result.rb'
  end
end