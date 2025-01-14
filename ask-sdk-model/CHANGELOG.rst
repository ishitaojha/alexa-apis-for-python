=========
CHANGELOG
=========

0.1
---

* Initial release of models.

0.1.1
~~~~~

* Docstring changes for generated docs.

0.2
---

* APIs for customer contact permissions (CCP).

0.2.1
~~~~~

* Bug fixes, removed incorrect models.

0.3.0
~~~~~

* APIs for getting device timezone, distance measurement, temperature measurement

1.0.0
-----

* Production release of ASK Models Package.

1.1.0
~~~~~

* Models for "Consumables" in In-Skill Products.

* APIs for Amazon Pay V2 that includes :

  - No consent token requirement in request.
  - Have billing address details for eligible Amazon Pay merchants in Response.
  - Permission scope addition to Permissions object.

* Update Skill Event Models to include additional attributes like 'eventPublishingTime' etc.

1.2.0
~~~~~

* Models for "PrintRequest" and "ReservationRequest" in Skill Connections.

1.3.0
~~~~~

* Models for "Alexa Presentation Language". The Alexa Presentation Language
  (APL) enables you to build interactive voice experiences that include
  graphics, images, slideshows, and video, and to customize them for
  different device types.



1.4.0
~~~~~~~

This release includes the following:
- Models for [CanFulfillIntentRequest, for Name-free Interactions](https://developer.amazon.com/docs/custom-skills/implement-canfulfillintentrequest-for-name-free-interaction.html)


1.5.0
~~~~~~~

This release includes the following : 

- Models for Location Services.
- Updated models for Game engine interface.


1.5.1
^^^^^^^

This release includes the following:

- Updated interfaces for Location Services


1.6.0
~~~~~~~

This release includes the following : 

- Models for Reminders


1.6.1
^^^^^^^

This release contains the following changes:

- Updated enum values for Reminder Status
- Updated OutputSpeech model


1.6.2
^^^^^^^

This release contains the following : 

- Updated enum values for APL components.


1.7.0
~~~~~~~

This release contains the following changes : 

- Support for proactive event calls from out of skill session.
- Remove delete reminders support.


1.8.0
~~~~~~~

This release contains the following changes :

- Introduces support for customizing your skill's experience for Echo Auto, which is now shipping to select customers via our invite program, and vehicles and other aftermarket devices that support Alexa Auto.
- The automotive experience introduces another way for customers to interact with skills, while they are on-the-go and their attention is on the road. Now you can adapt your skill experience to be succinct, location-aware, and adaptive to your customer's needs while they're outside the home.


1.9.0
~~~~~~~

This release contains the following changes : 

- Dynamic entities for customized interactions
- Add additional 'entitlementReason' field in In-Skill products


1.10.0
~~~~~~~

This release contains the following changes :

- The `Skill Messaging API <https://developer.amazon.com/docs/smapi/skill-messaging-api-reference.html>`__ is now supported. Use the Skill Messaging API to send a message request to a skill for a specified user. 
- Adds support for additional `APL Standard Commands <https://developer.amazon.com/docs/alexa-presentation-language/apl-standard-commands.html>`__.
- Packaged type information in models as per `PEP 0561 <https://www.python.org/dev/peps/pep-0561/>`__.


1.10.1
^^^^^^^

This release includes the following : 

- Fixing the imports under `reminder_management` service, to deserialize the reminders correctly.



1.10.2
^^^^^^^

- Added video codecs information in the APL Viewport Characteristic `Video property <https://developer.amazon.com/docs/alexa-presentation-language/apl-viewport-characteristics.html#video>`__. 


1.10.3
^^^^^^^

This release contains the following changes:

- Fix the `deserialized_type` for viewport_state.video object



1.11.0
~~~~~~~

This release contains the following changes : 

- APL `SetValue <https://developer.amazon.com/docs/alexa-presentation-language/apl-standard-commands.html#setvalue-command>`__ command support.



1.12.0
~~~~~~~

This release contains the following changes : 

- Added APL commands `AnimateItemCommand`, `OpenUrlCommand`, `SetFocusCommand`, `ClearFocusCommand`.
- Added `finally` and `catch` attributes in `SequentialCommand`.
- Provide APL expression language in some APL commands, alongside their primitive types (eg: `delay` in all commands).
- Added `ENDPOINT_TIMEOUT` enumeration in `SessionEndedReason`.



1.13.0
~~~~~~~

This release contains the following changes : 

-  Models for `Skill Connections <https://developer.amazon.com/docs/custom-skills/skill-connections.html>`__. With the Skill Connections feature, you can enable an Alexa skill to fulfill a customer request that it can't otherwise handle by forwarding the request to another skill for fulfillment. 


1.14.0
~~~~~~~

This release contains the following changes : 

-  Models for [Custom interfaces](https://developer.amazon.com/docs/alexa-gadgets-toolkit-preview/custom-interface.html). The custom interfaces feature enables Alexa Skill Developers to implement interactions between skills and gadgets using developer-defined directives and events.

-  Added BillingAgreementType and SubscriptionAmount in BillingAgreementAttributes. This change is mandatory for skills in EU, and optional for NA and JP. With this upgrade, skill developers in EU can enjoy full benefits of the Amazon Pay solution that supports PSD2.


1.15.0
~~~~~~~

This release contains the following changes : 
- A new `mode property <https://developer.amazon.com/docs/alexa-presentation-language/apl-viewport-property.html#viewport_mode_property>`__ in APL viewports
- The `gadget endpoint enumeration service <https://developer.amazon.com/es/docs/alexa-gadgets-toolkit/send-gadget-custom-directive-from-skill.html#call-endpoint-enumeration-api>`__
- Fixing a bug in base service client that leads to exceptions for a HTTP 204 response.


1.16.0
~~~~~~~

This release has the following changes : 

- Support for building APL-T Documents (APL Character displays).


1.17.0
~~~~~~~

This release contains the following changes : 

- APIs for `ISP support in kid skills <https://developer.amazon.com/docs/in-skill-purchase/isp-kid-skills.html>`__.


1.18.0
~~~~~~~

This release contains the following changes: 

- support for `personalization <https://developer.amazon.com/docs/custom-skills/add-personalization-to-your-skill.html#invocation-request-examples>`__ in the skill.


1.18.1
^^^^^^^

This release contains the following changes : 

- Models for APL visual context.


1.19.0
~~~~~~~

This release contains the following changes : 

- Alexa Presentation Language HTML Interface support. Apply for preview request `here <https://build.amazonalexadev.com/AlexaWebAPIforGamesDeveloperPreview_AlexaWebAPIforGames.html>`__.
- Update service client methods to return an `ApiResponse` instance, in case a full response is required instead of just the response body. 
- mypy fix for `AuthenticationConfiguration` class.


1.20.0
~~~~~~

This release contains the following changes : 

 - captions support in `audioplayer play directive <https://developer.amazon.com/docs/custom-skills/audioplayer-interface-reference.html#play>`__.


1.20.1
^^^^^^

This release contains the following changes : 

 - Missing objects added back from earlier minor release for caption data. 


1.20.2
^^^^^^

This release contains the following changes : 

- Fix the discriminator value for Alexa HTML message request object.
- Add Alexa HTML Runtime Error definitions.


1.21.0
~~~~~~

This release contains the following changes : 

- Updated `rules for recurrence creation <https://developer.amazon.com/en-US/docs/alexa/smapi/alexa-reminders-api-reference.html#in-session-and-out-of-session-behavior-for-alexa-reminders-api>`__ in reminders. 


1.22.0
~~~~~~

This release contains the following changes : 

- APIs related to `timer management <https://developer.amazon.com/en-US/docs/alexa/smapi/alexa-timers-api-reference.html>`__.



1.23.0
~~~~~~

This release contains the following changes : 

- Support for the next version of the Alexa Presentation Language (APL) with support for new Alexa responsive components and templates, dynamic data sources, new time primitives, and conditional commands. `Ref <https://developer.amazon.com/en-US/blogs/alexa/alexa-skills-kit/2020/03/new-alexa-presentation-language-responsive-components-templates-dynamic-data-sources-new-time-primitives-and-commands>`__.


1.23.1
^^^^^^

This release contains the following changes : 

- general bug fixes and updates


1.24.0
~~~~~~

This release contains the following changes :

- general bug fixes and updates


1.25.0
~~~~~~

This release contains the following changes :

- Introducing `person-level permissions <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-events-in-alexa-skills.html#skill-permission-changed-event>`__ for Skill events.


1.26.0
~~~~~~

This release contains the following changes : 

- Support for 'Alexa for residential' properties. More information about 'Alexa for residential' can be found here : https://developer.amazon.com/en-US/docs/alexa/alexa-smart-properties/about-alexa-for-residential.html


1.27.0
~~~~~~

This release contains the following changes :
- Add “onCompletion” field in Connections.StartConnection directive. When sending this directive to start a Skill Connection, requester skill can set onCompletion to be RESUME_SESSION to receive the control back after the task is completed or SEND_ERRORS_ONLY to only receive error notifications without control back. More information about using Skill Connections to Request Tasks can be found `here <https://developer.amazon.com/en-US/docs/alexa/custom-skills/use-skill-connections-to-request-tasks.html>`__.
- Add “Authorization.Grant” directive support for user specific access token in out-of-session calls. More information can be found `here <https://developer.amazon.com/en-US/docs/alexa/custom-skills/get-a-user-specific-access-token.html>`__.


1.28.0
~~~~~~

This release contains the following changes :

- Models and support for Extensions interfaces.


1.28.1
^^^^^^

This release contains the following changes : 

- Updating model definitions


1.29.0
~~~~~~

This release contains the following changes :
- APL for Audio now sends RuntimeError requests that notify developer of any errors that happened during APLA processing.


1.30.0
~~~~~~

This release contains the following changes :

- Add support for APL 1.6 version. More information about the newest version can be found `here <https://developer.amazon.com/en-US/docs/alexa/alexa-presentation-language/apl-latest-version.html>`__.




1.30.1
^^^^^^

This release contains the following changes :

- Adding missing definitions for APL 1.6. More information can be found `here <https://developer.amazon.com/en-US/docs/alexa/alexa-presentation-language/apl-latest-version.html#token-based-lazy-loading>`__.


1.31.0
~~~~~~

This release includes the following:

- Adding support for directives in Reprompt


1.31.1
^^^^^^

This release contains the following changes : 

- Updating model definitions

