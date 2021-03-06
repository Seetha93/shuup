# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.signals import Signal

# Modifying signals
from shuup.core.signals import get_basket_command_handler  # noqa

# Completion signals
order_complete_viewed = Signal(providing_args=["order", "request"], use_caching=True)
